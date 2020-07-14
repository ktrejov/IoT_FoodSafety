##SUMMER 2020
import paho.mqtt.client as mqtt
import time
from data_update import *

MIN_TEMP = 32
MAX_TEMP = 50
LAST_LEN = 24


lastList = "last_list.csv"


BROKER = "broker.mqttdashboard.com"
SUSCRIBE_TOPIC = "abhg/IoT/Test/Topic/ESP_Out"
PUBLISH_TOPIC = "abhg/IoT/Test/Topic/ESP_In"
WARNING_TOPIC = "abhg/IoT/Test/Topic/ESP_In/Warning"
DF="Temp_data.csv"

ENTRIES = ["Temperature","Date"]
    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(SUSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = str(msg.payload)
    message = message[2:-1]
    try:
        temp = int(message)/100
        localtime = str(time.asctime(time.localtime(time.time())))
        add_data(temp,localtime,DF,ENTRIES)
        add_data(temp,localtime,lastList,ENTRIES)
        if find_len(lastList) > LAST_LEN:
            value_del(lastList)
        if not MIN_TEMP < temp < MAX_TEMP:
            print("WARNING")
    except:
            pass

client= mqtt.Client(transport="websockets")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 8000, 60)
check_df(DF,ENTRIES)
check_df(lastList,ENTRIES)
client.loop_forever()


