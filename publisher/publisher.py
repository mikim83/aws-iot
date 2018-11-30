import ssl
import time
import json

# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

MQTT_TOPIC = "iotbutton/publishScript"
rawmessage = {}
rawmessage['serialNumber'] = "publishScript"
rawmessage['clickType'] = "SINGLE"
rawmessage['batteryVoltage'] = "2000 mV"

MQTT_MSG = json.dumps(rawmessage)

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("publisherScript")
myMQTTClient.configureEndpoint("a27ogmup3q9tz-ats.iot.eu-west-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("root-CA.crt", "private.pem.key", "certificate.pem.crt")


myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(5)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
myMQTTClient.configureAutoReconnectBackoffTime(1, 250, 20)  #original 32


myMQTTClient.connect()
myMQTTClient.publish(MQTT_TOPIC, MQTT_MSG, 0)
myMQTTClient.disconnect()