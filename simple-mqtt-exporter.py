#!/usr/bin/env python3
import os
import sys
import time
import paho.mqtt.client as mqtt
import prometheus_client as prom
import argparse
import importlib

def on_connect(client, userdata, flags, rc):
  codes = [
    'Connection successful',
    'Connection refused – incorrect protocol version',
    'Connection refused – invalid client identifier',
    'Connection refused – server unavailable',
    'Connection refused – bad username or password',
    'Connection refused – not authorised',
  ]
  if rc!=0:
    if rc > 0 and rc < 6:
      print(codes[rc])
    else:
      print(f'Bad connection, unknown return code: {rc}')
    os._exit(1)

def on_message(client, userdata, msg):
  global data_received, succes, error
  if config.debug:
    print(f'{msg.topic}: {payload}')
  if msg.topic in config.mqtt_topics:
    try:
      payload = str(msg.payload.decode("utf-8","strict"))
      value = float(payload)
      succes[t] += 1
      received_messages.labels(status='succes', topic=msg.topic).set(succes[t])
    except Exception as e:
      print(f'{type(e)}: {str(e)} while decoding topic {t}')
      error[t] += 1
      received_messages.labels(status='error', topic=msg.topic).set(error[t])
      return
    data_received = True
    gauges[msg.topic].set(value)
    updated.set(time.time())

def mqtt_init():
  client = mqtt.Client()
  if hasattr(config, 'mqtt_username') and hasattr(config, 'mqtt_password'):
    client.username_pw_set(config.mqtt_username, config.mqtt_password)
  client.on_connect=on_connect
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
  client = mqtt_init()
  succes = {}
  error = {}
  parents = {}
  gauges = {}
  for t,v in config.mqtt_topics.items():
    succes[t] = 0
    error[t] = 0
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
  received_messages = prom.Gauge('received_messages', 'received messages per topic and status', ['status','topic'])
  prom.start_http_server(config.http_port)

  fresh = time.time()
  while True:
    data_received = False
    time.sleep(10)
    if data_received:
      up.set(1)
      fresh = time.time()
    else:
      up.set(0)
      if not client.is_connected() and time.time() - fresh > 600:
        print(f"Exiting, mqtt state = {client._state} for too long")
        sys.exit(1)
