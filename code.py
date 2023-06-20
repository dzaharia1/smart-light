import time
import board
import feeds
import lights
from secrets import secrets

def message(client, feed_id, payload):
    if feed_id == feeds.colorFeed:
        lights.setColor(payload)
        
    if feed_id == feeds.brightnessFeed:
        lights.setBrightness(payload)
        
    if feed_id == feeds.statusFeed:
        if payload == "OFF":
            lights.setBrightness(0)
            
    if feed_id == feeds.effectFeed:
        print("Got {} on effect feed".format(payload))
        if payload == "Blast":
            lights.pixels.fill((255, 255, 255, 200))

feeds.mqttClient.on_message = message

while True:
    feeds.mqttClient.ping()
    try:
        feeds.mqttClient.loop(timeout=40)
    except:
        feeds.wifi.radio.connect(secrets["ssid"], secrets["password"])
        feeds.mqttClient.reconnect(resub_topics=False)
        feeds.mqttClient.subscribe([(feeds.statusFeed, 0), (feeds.brightnessFeed, 0), (feeds.colorFeed, 0), (feeds.effectFeed, 0)])


