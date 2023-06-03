#!/usr/bin/env python3
import sys
import time
import paho.mqtt.client as mqtt
import prometheus_client as prom
import argparse
import importlib

def on_message(client, userdata, msg):
  global dataReceived
  payload = str(msg.payload.decode("utf-8","ignore"))
  if config.debug:
    print(f'{msg.topic}: {payload}')
  if msg.topic in config.mqtt_topics:
    dataReceived = True
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
    name = v.get('name')
    if not name:
      name = t.split('/')[-1:][0]
    helptext = v.get('help')
    if not helptext:
      helptext = t
    labels = v.get('labels', {})
    if not name in parents:
      parents[name] = prom.Gauge(name, helptext, labels.keys())
    if labels:
      gauges[t] = parents[name].labels(**labels)
    else:
      gauges[t] = parents[name]
  up = prom.Gauge('up', 'client status')
  updated = prom.Gauge('updated', 'data last updated in epoch')
  prom.start_http_server(config.http_port)

  while True:
    dataReceived = False
    time.sleep(10)
    if dataReceived:
      up.set(1)
    else:
      up.set(0)
