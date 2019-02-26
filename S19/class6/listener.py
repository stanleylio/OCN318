# Listen in to the 'uhm/soest/ocn318/#' topic and print all messages to screen.
#
# Lots of free brokers out there. Be nice (don't spam).
#   https://github.com/mqtt/mqtt.github.io/wiki/public_brokers
#
# We will use one of these:
#   iot.eclipse.org
#   test.mosquitto.org
#   broker.hivemq.com
#
# pip3 install --upgrade paho-mqtt
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    #print('code ' + str(rc))
    #client.subscribe('$SYS/#')
    client.subscribe('uhm/soest/ocn318/#')

def on_message(client, userdata, msg):
    print(msg.topic + '\t' + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('broker.hivemq.com', port=1883, keepalive=60)

client.loop_forever()
