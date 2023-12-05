# to be used together with https://github.com/RichieB2B/overkiz2mqtt
# mqtt broker
mqtt_broker="127.0.0.1"
mqtt_username="me"
mqtt_password="secret"
mqtt_topic = "cozytouch/#"

# http server
http_port = 8078

# dict with topic as key and dict value with name, labels and help.
# If name is omitted, the last part of the topic will be used.
# If help is omitted, the full topic name will be used.
# If lables are omitted, no labels are used.
# 'topic1': { 'name': 'my_topic1', 'labels': {'label1': 'foo', 'label2': 'bar'}, help: 'power in Watt' },
# 'topic2': { 'help': 'voltage' },
# 'topic3': { 'name': 'my_topics3', 'labels': {'label1': 'baz'} },
# 'topic4': {},
mqtt_topics = {
  'cozytouch/io:AtlanticDomesticHotWaterProductionV2_CV4E_IOComponent/states': [
    {'field': 'core:RSSILevelState', 'name': 'wpb_rssilevel_db', 'help': 'RSSI level in dB'},
    {'field': 'core:TemperatureState', 'name': 'wpb_temperature_celsius', 'labels': {'type': 'wanted'}, 'help': 'Temperature in degrees Celsius'},
    {'field': 'core:TargetTemperatureState', 'name': 'wpb_temperature_celsius', 'labels': {'type': 'target'}, 'help': 'Temperature in degrees Celsius'},
    {'field': 'core:V40WaterVolumeEstimationState', 'name': 'wpb_watervolumeestimation_l', 'help': 'Volume in liter'},
    {'field': 'io:MiddleWaterTemperatureState', 'name': 'wpb_temperature_celsius', 'labels': {'type': 'middle'}, 'help': 'Temperature in degrees Celsius'},
    {'field': 'io:HeatPumpOperatingTimeState', 'name': 'wpb_operatingtime_hour', 'labels': {'object': 'heatpump'}, 'help': 'Operating time in hours'},
    {'field': 'io:ElectricBoosterOperatingTimeState', 'name': 'wpb_operatingtime_hour', 'labels': {'object': 'booster'}, 'help': 'Operating time in hours'},
    {'field': 'io:PowerHeatElectricalState', 'name': 'wpb_power_watt', 'labels': {'type': 'electrical'}, 'help': 'Power in Watt'},
    {'field': 'io:PowerHeatPumpState', 'name': 'wpb_power_watt', 'labels': {'type': 'heatpump'}, 'help': 'Power in Watt'},
    {'field': 'core:BoostModeDurationState', 'name': 'wpb_duration_day', 'labels': {'type': 'boostmode'}, 'help': 'Duration in days'},
    {'field': 'io:AwayModeDurationState', 'name': 'wpb_duration_day', 'labels': {'type': 'awaymode'}, 'help': 'Duration in days'},
  ],
  'cozytouch/internal:PodMiniComponent/states': [
    {'field': 'internal:LightingLedPodModeState', 'name': 'wpb_ledpodmode'},
  ],
  'cozytouch/io:DHWCumulatedElectricalEnergyConsumptionIOSystemDeviceSensor/states': [
    {'field': 'core:ElectricEnergyConsumptionState', 'name': 'wpb_energyconsumption_wh', 'help': 'Electric energy consumption in Wh'},
  ],
}

sleep = 30

debug = False
