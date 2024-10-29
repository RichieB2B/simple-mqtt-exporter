# mqtt broker where tasmota devices publish their data
mqtt_broker = "127.0.0.1"
mqtt_username = "me"
mqtt_password = "secret"
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
    "tasmota/tele/.*/STATE": [
        {"field": "UptimeSec", "name": "uptime", "help": "uptime in seconds"},
        {"field": "Heap", "name": "tasmota_heap", "help": "heap size"},
        {"field": "Sleep", "name": "tasmota_sleep", "help": "sleep in percentage"},
        {"field": "LoadAvg", "name": "tasmota_load_average", "help": "load average"},
        {"field": "MqttCount", "name": "tasmota_mqtt_count", "help": "MQTT counter"},
        {
            "field": "POWER",
            "name": "tasmota_power_switch_state",
            "help": "power switch state",
        },
    ],
    "tasmota/tele/.*/SENSOR": [
        {
            "field": "ANALOG.Temperature",
            "name": "tasmota_temperature",
            "help": "temperature in Celsius",
        },
        {"field": "ENERGY.Power", "name": "tasmota_power", "help": "power in Watt"},
        {
            "field": "ENERGY.Voltage",
            "name": "tasmota_voltage",
            "help": "voltage in Volt",
        },
        {
            "field": "ENERGY.Current",
            "name": "tasmota_current",
            "help": "current in Ampere",
        },
    ],
}

sleep = 60

debug = False
