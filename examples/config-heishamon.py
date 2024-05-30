# mqtt broker where Heishamon publishes its topics
mqtt_broker="127.0.0.1"
#mqtt_username="user"
#mqtt_password="pass
mqtt_topic = "panasonic_heat_pump/#"

# http server
http_port = 8073

# dict with topic as key and dict value with name, labels and help.
# If name is omitted, the last part of the topic will be used.
# If help is omitted, the full topic name will be used.
# If lables are omitted, no labels are used.
# 'topic1': { 'name': 'my_topic1', 'labels': {'label1': 'foo', 'label2': 'bar'}, help: 'power in Watt' },
# 'topic2': { 'help': 'voltage' },
# 'topic3': { 'name': 'my_topics3', 'labels': {'label1': 'baz'} },
# 'topic4': {},

# See https://github.com/IgorYbema/HeishaMon/blob/main/MQTT-Topics.md for a full legend
mqtt_topics = {
  'panasonic_heat_pump/LWT': {'name': 'LWT'},
  'panasonic_heat_pump/main/Alt_External_Sensor': {'name': 'alt_external_sensor'},
  'panasonic_heat_pump/main/Anti_Freeze_Mode': {'name': 'anti_freeze_mode'},
  'panasonic_heat_pump/main/Buffer_Installed': {'name': 'buffer_installed'},
  'panasonic_heat_pump/main/Buffer_Tank_Delta': {'name': 'buffer_tank_delta'},
  'panasonic_heat_pump/main/Buffer_Temp': {'name': 'buffer_temp'},
  'panasonic_heat_pump/main/Bypass_Outlet_Temp': {'name': 'bypass_outlet_temp'},
  'panasonic_heat_pump/main/Compressor_Current': {'name': 'compressor_current'},
  'panasonic_heat_pump/main/Compressor_Freq': {'name': 'compressor_freq'},
  'panasonic_heat_pump/main/Cool_Delta': {'name': 'cool_delta'},
  'panasonic_heat_pump/main/Cool_Power_Consumption': {'name': 'cool_power_consumption'},
  'panasonic_heat_pump/main/Cool_Power_Production': {'name': 'cool_power_production'},
  'panasonic_heat_pump/main/Cool_To_Heat_Temp': {'name': 'cool_to_heat_temp'},
  'panasonic_heat_pump/main/Cooling_Mode': {'name': 'cooling_mode'},
  'panasonic_heat_pump/main/DHW_Heat_Delta': {'name': 'dhw_heat_delta'},
  'panasonic_heat_pump/main/DHW_Heater_Operations_Hours': {'name': 'dhw_heater_operations_hours'},
  'panasonic_heat_pump/main/DHW_Heater_State': {'name': 'dhw_heater_state'},
  'panasonic_heat_pump/main/DHW_Holiday_Shift_Temp': {'name': 'dhw_holiday_shift_temp'},
  'panasonic_heat_pump/main/DHW_Installed': {'name': 'dhw_installed'},
  'panasonic_heat_pump/main/DHW_Power_Consumption': {'name': 'dhw_power_consumption'},
  'panasonic_heat_pump/main/DHW_Power_Production': {'name': 'dhw_power_production'},
  'panasonic_heat_pump/main/DHW_Target_Temp': {'name': 'dhw_target_temp'},
  'panasonic_heat_pump/main/DHW_Temp': {'name': 'dhw_temp'},
  'panasonic_heat_pump/main/Defrost_Temp': {'name': 'defrost_temp'},
  'panasonic_heat_pump/main/Defrosting_State': {'name': 'defrosting_state'},
  'panasonic_heat_pump/main/Discharge_Temp': {'name': 'discharge_temp'},
  'panasonic_heat_pump/main/Economizer_Outlet_Temp': {'name': 'economizer_outlet_temp'},
  'panasonic_heat_pump/main/Eva_Outlet_Temp': {'name': 'eva_outlet_temp'},
  'panasonic_heat_pump/main/External_Heater_State': {'name': 'external_heater_state'},
  'panasonic_heat_pump/main/External_Pad_Heater': {'name': 'external_pad_heater'},
  'panasonic_heat_pump/main/Fan1_Motor_Speed': {'name': 'fan1_motor_speed'},
  'panasonic_heat_pump/main/Fan2_Motor_Speed': {'name': 'fan2_motor_speed'},
  'panasonic_heat_pump/main/Force_DHW_State': {'name': 'force_dhw_state'},
  'panasonic_heat_pump/main/Force_Heater_State': {'name': 'force_heater_state'},
  'panasonic_heat_pump/main/Heat_Delta': {'name': 'heat_delta'},
  'panasonic_heat_pump/main/Heat_Power_Consumption': {'name': 'heat_power_consumption'},
  'panasonic_heat_pump/main/Heat_Power_Production': {'name': 'heat_power_production'},
  'panasonic_heat_pump/main/Heat_Pump_Model': {'name': 'heat_pump_model'},
  'panasonic_heat_pump/main/Heat_To_Cool_Temp': {'name': 'heat_to_cool_temp'},
  'panasonic_heat_pump/main/Heater_Delay_Time': {'name': 'heater_delay_time'},
  'panasonic_heat_pump/main/Heater_On_Outdoor_Temp': {'name': 'heater_on_outdoor_temp'},
  'panasonic_heat_pump/main/Heater_Start_Delta': {'name': 'heater_start_delta'},
  'panasonic_heat_pump/main/Heater_Stop_Delta': {'name': 'heater_stop_delta'},
  'panasonic_heat_pump/main/Heating_Mode': {'name': 'heating_mode'},
  'panasonic_heat_pump/main/Heating_Off_Outdoor_Temp': {'name': 'heating_off_outdoor_temp'},
  'panasonic_heat_pump/main/Heatpump_State': {'name': 'heatpump_state'},
  'panasonic_heat_pump/main/High_Pressure': {'name': 'high_pressure'},
  'panasonic_heat_pump/main/Holiday_Mode_State': {'name': 'holiday_mode_state'},
  'panasonic_heat_pump/main/Inside_Pipe_Temp': {'name': 'inside_pipe_temp'},
  'panasonic_heat_pump/main/Internal_Heater_State': {'name': 'internal_heater_state'},
  'panasonic_heat_pump/main/Ipm_Temp': {'name': 'ipm_temp'},
  'panasonic_heat_pump/main/Liquid_Type': {'name': 'liquid_type'},
  'panasonic_heat_pump/main/Low_Pressure': {'name': 'low_pressure'},
  'panasonic_heat_pump/main/Main_Hex_Outlet_Temp': {'name': 'main_hex_outlet_temp'},
  'panasonic_heat_pump/main/Main_Inlet_Temp': {'name': 'main_inlet_temp'},
  'panasonic_heat_pump/main/Main_Outlet_Temp': {'name': 'main_outlet_temp'},
  'panasonic_heat_pump/main/Main_Schedule_State': {'name': 'main_schedule_state'},
  'panasonic_heat_pump/main/Main_Target_Temp': {'name': 'main_target_temp'},
  'panasonic_heat_pump/main/Max_Pump_Duty': {'name': 'max_pump_duty'},
  'panasonic_heat_pump/main/Operating_Mode_State': {'name': 'operating_mode_state'},
  'panasonic_heat_pump/main/Operations_Counter': {'name': 'operations_counter'},
  'panasonic_heat_pump/main/Operations_Hours': {'name': 'operations_hours'},
  'panasonic_heat_pump/main/Optional_PCB': {'name': 'optional_pcb'},
  'panasonic_heat_pump/main/Outside_Pipe_Temp': {'name': 'outside_pipe_temp'},
  'panasonic_heat_pump/main/Outside_Temp': {'name': 'outside_temp'},
  'panasonic_heat_pump/main/Pool_Temp': {'name': 'pool_temp'},
  'panasonic_heat_pump/main/Powerful_Mode_Time': {'name': 'powerful_mode_time'},
  'panasonic_heat_pump/main/Pump_Duty': {'name': 'pump_duty'},
  'panasonic_heat_pump/main/Pump_Flow': {'name': 'pump_flow'},
  'panasonic_heat_pump/main/Pump_Flowrate_Mode': {'name': 'pump_flowrate_mode'},
  'panasonic_heat_pump/main/Pump_Speed': {'name': 'pump_speed'},
  'panasonic_heat_pump/main/Quiet_Mode_Level': {'name': 'quiet_mode_level'},
  'panasonic_heat_pump/main/Quiet_Mode_Schedule': {'name': 'quiet_mode_schedule'},
  'panasonic_heat_pump/main/Room_Heater_Operations_Hours': {'name': 'room_heater_operations_hours'},
  'panasonic_heat_pump/main/Room_Heater_State': {'name': 'room_heater_state'},
  'panasonic_heat_pump/main/Room_Holiday_Shift_Temp': {'name': 'room_holiday_shift_temp'},
  'panasonic_heat_pump/main/Room_Thermostat_Temp': {'name': 'room_thermostat_temp'},
  'panasonic_heat_pump/main/Second_Inlet_Temp': {'name': 'second_inlet_temp'},
  'panasonic_heat_pump/main/Second_Room_Thermostat_Temp': {'name': 'second_room_thermostat_temp'},
  'panasonic_heat_pump/main/Solar_Frost_Protection': {'name': 'solar_frost_protection'},
  'panasonic_heat_pump/main/Solar_High_Limit': {'name': 'solar_high_limit'},
  'panasonic_heat_pump/main/Solar_Mode': {'name': 'solar_mode'},
  'panasonic_heat_pump/main/Solar_Off_Delta': {'name': 'solar_off_delta'},
  'panasonic_heat_pump/main/Solar_On_Delta': {'name': 'solar_on_delta'},
  'panasonic_heat_pump/main/Solar_Temp': {'name': 'solar_temp'},
  'panasonic_heat_pump/main/Sterilization_Max_Time': {'name': 'sterilization_max_time'},
  'panasonic_heat_pump/main/Sterilization_State': {'name': 'sterilization_state'},
  'panasonic_heat_pump/main/Sterilization_Temp': {'name': 'sterilization_temp'},
  'panasonic_heat_pump/main/ThreeWay_Valve_State': {'name': 'threeway_valve_state'},
  'panasonic_heat_pump/main/Water_Pressure': {'name': 'water_pressure'},
  'panasonic_heat_pump/main/Z1_Cool_Curve_Outside_High_Temp': {'name': 'z1_cool_curve_outside_high_temp'},
  'panasonic_heat_pump/main/Z1_Cool_Curve_Outside_Low_Temp': {'name': 'z1_cool_curve_outside_low_temp'},
  'panasonic_heat_pump/main/Z1_Cool_Curve_Target_High_Temp': {'name': 'z1_cool_curve_target_high_temp'},
  'panasonic_heat_pump/main/Z1_Cool_Curve_Target_Low_Temp': {'name': 'z1_cool_curve_target_low_temp'},
  'panasonic_heat_pump/main/Z1_Cool_Request_Temp': {'name': 'z1_cool_request_temp'},
  'panasonic_heat_pump/main/Z1_Heat_Curve_Outside_High_Temp': {'name': 'z1_heat_curve_outside_high_temp'},
  'panasonic_heat_pump/main/Z1_Heat_Curve_Outside_Low_Temp': {'name': 'z1_heat_curve_outside_low_temp'},
  'panasonic_heat_pump/main/Z1_Heat_Curve_Target_High_Temp': {'name': 'z1_heat_curve_target_high_temp'},
  'panasonic_heat_pump/main/Z1_Heat_Curve_Target_Low_Temp': {'name': 'z1_heat_curve_target_low_temp'},
  'panasonic_heat_pump/main/Z1_Heat_Request_Temp': {'name': 'z1_heat_request_temp'},
  'panasonic_heat_pump/main/Z1_Sensor_Settings': {'name': 'z1_sensor_settings'},
  'panasonic_heat_pump/main/Z1_Temp': {'name': 'z1_temp'},
  'panasonic_heat_pump/main/Z1_Water_Target_Temp': {'name': 'z1_water_target_temp'},
  'panasonic_heat_pump/main/Z1_Water_Temp': {'name': 'z1_water_temp'},
  'panasonic_heat_pump/main/Z2_Cool_Curve_Outside_High_Temp': {'name': 'z2_cool_curve_outside_high_temp'},
  'panasonic_heat_pump/main/Z2_Cool_Curve_Outside_Low_Temp': {'name': 'z2_cool_curve_outside_low_temp'},
  'panasonic_heat_pump/main/Z2_Cool_Curve_Target_High_Temp': {'name': 'z2_cool_curve_target_high_temp'},
  'panasonic_heat_pump/main/Z2_Cool_Curve_Target_Low_Temp': {'name': 'z2_cool_curve_target_low_temp'},
  'panasonic_heat_pump/main/Z2_Cool_Request_Temp': {'name': 'z2_cool_request_temp'},
  'panasonic_heat_pump/main/Z2_Heat_Curve_Outside_High_Temp': {'name': 'z2_heat_curve_outside_high_temp'},
  'panasonic_heat_pump/main/Z2_Heat_Curve_Outside_Low_Temp': {'name': 'z2_heat_curve_outside_low_temp'},
  'panasonic_heat_pump/main/Z2_Heat_Curve_Target_High_Temp': {'name': 'z2_heat_curve_target_high_temp'},
  'panasonic_heat_pump/main/Z2_Heat_Curve_Target_Low_Temp': {'name': 'z2_heat_curve_target_low_temp'},
  'panasonic_heat_pump/main/Z2_Heat_Request_Temp': {'name': 'z2_heat_request_temp'},
  'panasonic_heat_pump/main/Z2_Sensor_Settings': {'name': 'z2_sensor_settings'},
  'panasonic_heat_pump/main/Z2_Temp': {'name': 'z2_temp'},
  'panasonic_heat_pump/main/Z2_Water_Target_Temp': {'name': 'z2_water_target_temp'},
  'panasonic_heat_pump/main/Z2_Water_Temp': {'name': 'z2_water_temp'},
  'panasonic_heat_pump/main/Zones_State': {'name': 'zones_state'},
  'panasonic_heat_pump/stats': [
    {"field": "uptime", "name": "uptime"},
    {"field": "voltage", "name": "stats_voltage"},
    {"field": "free memory", "name": "stats_free_memory"},
    {"field": "free heap", "name": "stats_free_heap"},
    {"field": "wifi", "name": "stats_wifi"},
    {"field": "mqtt reconnects", "name": "stats_mqtt_reconnects"},
    {"field": "total reads", "name": "stats_total_reads"},
    {"field": "good reads", "name": "stats_good_reads"},
    {"field": "bad crc reads", "name": "stats_bad_crc_reads"},
    {"field": "bad header reads", "name": "stats_bad_header_reads"},
    {"field": "too short reads", "name": "stats_too_short_reads"},
    {"field": "too long reads", "name": "stats_too_long_reads"},
    {"field": "timeout reads", "name": "stats_timeout_reads"},
    {"field": "version", "name": "stats_version"},
    {"field": "rules active", "name": "stats_rules_active"},
  ]
}

debug = False
