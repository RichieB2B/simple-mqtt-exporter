# mqtt broker where TWC publishes its topics
mqtt_broker="127.0.0.1"
#mqtt_username="user"
#mqtt_password="pass"
mqtt_topic = "TWC/#"

# http server
http_port = 8086

# dict with topic as key and dict value with name, labels and help.
# If name is omitted, the last part of the topic will be used.
# If help is omitted, the full topic name will be used.
# If lables are omitted, no labels are used.
# 'topic1': { 'name': 'my_topic1', 'labels': {'label1': 'foo', 'label2': 'bar'}, help: 'power in Watt' },
# 'topic2': { 'help': 'voltage' },
# 'topic3': { 'name': 'my_topics3', 'labels': {'label1': 'baz'} },
# 'topic4': {},
mqtt_topics = {
  'TWC/all/maxAmpsForSlaves': {'help': 'Amps available for all TWCs'},
  'TWC/all/totalAmpsInUse': {'help': 'Amps in use by all TWCs'},
  'TWC/4242/ampsMax': {'help': 'maximum Amps for this TWC'},
  'TWC/4242/ampsInUse': {'help': 'Amps in use by this TWC'},
  'TWC/4242/chargerLoadInW': {'help': 'current load of this TWC in Watt'},
  'TWC/4242/state': {'help': 'TWC state code'},
  'TWC/4242/power': {'help': 'power in Watt'},
  'TWC/4242/carsCharging': {'help': 'number of cars currently charging'},
  'TWC/4242/lifetimekWh': {'help': 'lifetime usage in kWh'},
  'TWC/4242/voltagePhaseA': {'name': 'voltage', 'help': 'voltage in V', 'labels': {'phase': 'L1'}},
  'TWC/4242/voltagePhaseB': {'name': 'voltage', 'help': 'voltage in V', 'labels': {'phase': 'L2'}},
  'TWC/4242/voltagePhaseC': {'name': 'voltage', 'help': 'voltage in V', 'labels': {'phase': 'L3'}},
}

debug = False
