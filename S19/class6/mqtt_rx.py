# The S in IoT stands for security.
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    client.subscribe('uhm/soest/ocn318/#')

def on_message(client, userdata, msg):
    print(msg.topic + '\t' + msg.payload.decode())


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('broker.hivemq.com', port=1883, keepalive=60)

client.loop_forever()
