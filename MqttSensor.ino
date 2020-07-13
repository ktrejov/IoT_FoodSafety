#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DallasTemperature.h>

const char* ssid = "QoolOs";
const char* password = "Arbol5192!123";
const char* mqtt_server = "broker.mqttdashboard.com";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE (60)
char msg[MSG_BUFFER_SIZE];

const int oneWireBus = 4;
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

void setup_wifi() {

  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      //client.publish("abhg/IoT/Test/Topic/ESP_Out", "hello world");
      client.subscribe("abhg/IoT/Test/Topic/ESP_In/#");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  sensors.begin();
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    sensors.requestTemperatures();
    int temperatureF = sensors.getTempFByIndex(0)*100;
    snprintf (msg, MSG_BUFFER_SIZE, "%ld", temperatureF);
    Serial.print("Temperature: ");
    Serial.print(temperatureF);
    Serial.println("°F");
    client.publish("abhg/IoT/Test/Topic/ESP_Out",msg);
  }
}
