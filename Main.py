import paho.mqtt.client as mqtt
import time
import csv
from data_update import *

MIN_TEMP = 32
MAX_TEMP = 50
BROKER = "broker.mqttdashboard.com"
SUSCRIBE_TOPIC = "abhg/IoT/Test/Topic/ESP_Out"
PUBLISH_TOPIC = "abhg/IoT/Test/Topic/ESP_In"
WARNING_TOPIC = "abhg/IoT/Test/Topic/ESP_In/Warning"
DF='Temp_data.csv'
ENTRIES = ["Temperature","Date"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(SUSCRIBE_TOPIC)

def on_message(client, userdata, msg):
	message = str(msg.payload)
	message = message[2:-1]
	try:
		temp = float(message)
		localtime = str(time.asctime(time.localtime(time.time()))) #.split()
		add_data(temp,localtime,DF,ENTRIES)
		if not MIN_TEMP < temp < MAX_TEMP:
			print("Warning")
	except:
		pass

client= mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message
check_df(DF,ENTRIES)
client.connect(BROKER, 8000, 60)
client.loop_forever()	

