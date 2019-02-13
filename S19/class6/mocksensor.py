# mock-sensor
import paho.mqtt.client as mqtt
import random, time


client = mqtt.Client()

client.connect('broker.hivemq.com', port=1883, keepalive=60)
client.loop_start()

while True:
    t = random.random()*50
    client.publish('uhm/soest/ocn318/demo/temperature', t)

    time.sleep(1)
