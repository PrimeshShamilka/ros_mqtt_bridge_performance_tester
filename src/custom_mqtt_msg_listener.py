import paho.mqtt.client as mqtt
import json
import time

packets = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("ping")

def on_disconnect(client, userdata,rc=0):
    logging.debug("DisConnected result code "+str(rc))
    # client.loop_stop()

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print (msg.payload.decode('utf-8'))
    global packets
    packet = []    
    message = json.loads(msg.payload.decode('utf-8'))
    secs = message['header']['stamp']['secs']
    nsecs = message['header']['stamp']['nsecs']
    seq = message['header']['seq']
    packet = {'secs':secs,'nsecs':nsecs,'seq':seq}
    packets.append(packet)

    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("localhost", 1883, 60)
client.loop_start()

count1 = 0
while count1 < 150000000:
    count1+=1

client.loop_stop()

total_latency = 0
average_latency = 0
packet_loss = 0
sent_packet_count = 100
count2 = 0

for packet in packets:
    count2+=1
    sent_time = float(str(packet['secs']) + '.' + str(packet['nsecs']))
    total_latency += time.time() - sent_time

average_latency = total_latency/sent_packet_count
packet_loss = sent_packet_count - count2

print ("AVERAGE LATENCY: ",average_latency)
print ("PACKET_LOSS: ", packet_loss)