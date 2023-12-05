# mqtt broker where TWC published its topics
mqtt_broker="127.0.0.1"
#mqtt_username="user"
#mqtt_password="pass"
mqtt_topic = "mbmd/orno3p1-1/#"

# http server
http_port = 8087

# dict with topic as key and dict value with name, labels and help.
# If name is omitted, the last part of the topic will be used.
# If help is omitted, the full topic name will be used.
# If lables are omitted, no labels are used.
# 'topic1': { 'name': 'my_topic1', 'labels': {'label1': 'foo', 'label2': 'bar'}, help: 'power in Watt' },
# 'topic2': { 'help': 'voltage' },
# 'topic3': { 'name': 'my_topics3', 'labels': {'label1': 'baz'} },
# 'topic4': {},
mqtt_topics = {
  'mbmd/orno3p1-1/Power': {'name': 'mbmd_power', 'help': 'power consumption in Watt'},
  'mbmd/orno3p1-1/Import': {'name': 'mbmd_usage', 'help': 'energy usage in kWh'},
  'mbmd/orno3p1-1/Current/L1': {'name': 'mbmd_current', 'help': 'current in Ampere', 'labels': {'phase': 'L1'}},
  'mbmd/orno3p1-1/Current/L2': {'name': 'mbmd_current', 'help': 'current in Ampere', 'labels': {'phase': 'L2'}},
  'mbmd/orno3p1-1/Current/L3': {'name': 'mbmd_current', 'help': 'current in Ampere', 'labels': {'phase': 'L3'}},
  'mbmd/orno3p1-1/Voltage/L1': {'name': 'mbmd_voltage', 'help': 'voltage in Volt', 'labels': {'phase': 'L1'}},
  'mbmd/orno3p1-1/Voltage/L2': {'name': 'mbmd_voltage', 'help': 'voltage in Volt', 'labels': {'phase': 'L2'}},
  'mbmd/orno3p1-1/Voltage/L3': {'name': 'mbmd_voltage', 'help': 'voltage in Volt', 'labels': {'phase': 'L3'}},
}

debug = False
