# mqtt broker where tasmota devices publish their data
mqtt_broker="127.0.0.1"
mqtt_username="me"
mqtt_password="secret"
mqtt_topic = "tasmota/tele/#"

# http server
http_port = 8176

# dict with topic as key and dict value with name, labels and help.
# If name is omitted, the last part of the topic will be used.
# If help is omitted, the full topic name will be used.
# If lables are omitted, no labels are used.
# 'topic1': { 'name': 'my_topic1', 'labels': {'label1': 'foo', 'label2': 'bar'}, help: 'power in Watt' },
# 'topic2': { 'help': 'voltage' },
# 'topic3': { 'name': 'my_topics3', 'labels': {'label1': 'baz'} },
# 'topic4': {},

# This config uses a special regex topic. The string at the ".*" location sets
# the device label for all fields.
mqtt_topics = {
  'tasmota/tele/.*/STATE': [
    {'field': 'UptimeSec', 'name': 'uptime', 'help': 'Uptime in seconds'},
    {'field': 'Heap', 'name': 'tasmota_heap', 'help': 'heap size'},
    {'field': 'Sleep', 'name': 'tasmota_sleep', 'help': 'Sleep in percentage'},
    {'field': 'LoadAvg', 'name': 'tasmota_load_average', 'help': 'Load average'},
    {'field': 'MqttCount', 'name': 'tasmota_mqtt_count', 'help': 'MQTT counter'},
    {'field': 'POWER', 'name': 'tasmota_power_switch_state', 'help': 'Power switch state'},
  ]
}

sleep = 60

debug = False
