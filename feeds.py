import wifi
from secrets import secrets
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as MQTT

statusFeed = "box-light/switch"
brightnessFeed = "box-light/brightness/set"
colorFeed = "box-light/rgb/set"
effectFeed = "box-light/effect/set"

print("Connecting to {}".format(secrets["ssid"]))
wifi.radio.connect(secrets['ssid'], secrets['password'])

def connected(client, a, b, c):
    print("Connected to HA")

pool = socketpool.SocketPool(wifi.radio)

mqttClient = MQTT.MQTT(
    broker=secrets['mqtt_broker'],
    port=secrets['mqtt_port'],
    username=secrets['mqtt_username'],
    password=secrets['mqtt_password'],
    socket_pool=pool
)

def loop():
    print("looping")
    try:
        mqttClient.ping()
        print(mqttClient.loop(timeout=10))
    except:
        print("It broke")
        wifi.radio.connect(secrets['ssid'], secrets['password'])
        mqttClient.reconnect(resub_topics=False)
        mqttClient.subscribe([(statusFeed, 0), (brightnessFeed, 0), (colorFeed, 0), (effectFeed, 0)])

mqttClient.on_connect = connected

print("Connecting to HA")
mqttClient.connect()
mqttClient.subscribe([(statusFeed, 0), (brightnessFeed, 0), (colorFeed, 0), (effectFeed, 0)])

