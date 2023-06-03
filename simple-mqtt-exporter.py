#!/usr/bin/env python3
import sys
import time
import paho.mqtt.client as mqtt
import prometheus_client as prom
import argparse
import importlib

def on_message(client, userdata, msg):
  global data_received
  payload = str(msg.payload.decode("utf-8","ignore"))
  if config.debug:
    print(f'{msg.topic}: {payload}')
  if msg.topic in config.mqtt_topics:
    data_received = True
    received_messages.labels(msg.topic).inc()
    gauges[msg.topic].set(float(payload))
    updated.set(time.time())

def mqtt_init():
  client = mqtt.Client()
  if hasattr(config, 'mqtt_username') and hasattr(config, 'mqtt_password'):
    client.username_pw_set(config.mqtt_username, config.mqtt_password)
  client.on_message=on_message
  client.connect(config.mqtt_broker)
  client.subscribe(config.mqtt_twc_topic)
  client.loop_start()
  return client

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--config", help="config file to load", default="config")
  args = parser.parse_args()
  config = importlib.import_module(args.config)
  mqtt_init()
  parents = {}
  gauges = {}
  for t,v in config.mqtt_topics.items():
    parts = t.split('/')
    name = v.get('name')
    if not name:
      name = parts[-1:][0]
    description = v.get('help')
    if not description:
      description = t
    labels = v.get('labels', {})
    labels['topic'] = t
    if len(parts) > 0:
      labels['sensor'] = parts[1]
    if not name in parents:
      parents[name] = prom.Gauge(name, description, labels.keys())
    gauges[t] = parents[name].labels(**labels)
  up = prom.Gauge('up', 'client status')
  updated = prom.Gauge('updated', 'data last updated in epoch')
  received_messages = prom.Counter('received_messages', 'received messages per topic', ['topic'])
  prom.start_http_server(config.http_port)

  while True:
    data_received = False
    time.sleep(10)
    if data_received:
      up.set(1)
    else:
      up.set(0)
