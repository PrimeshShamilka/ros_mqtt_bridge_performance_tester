import paho.mqtt.client as mqtt
import json
import time
import rospy

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
    try:
        global packets
        packet = []    
        message = json.loads(msg.payload.decode('utf-8'))
        secs = message['header']['stamp']['secs']
        nsecs = message['header']['stamp']['nsecs']
        seq = message['header']['seq']

        sent_time = float(str(secs) + '.' + str(nsecs))
        ros_current_time = rospy.get_rostime()
        current_time = float(str(ros_current_time.secs) + '.' + str(ros_current_time.nsecs))
        print(current_time>sent_time)
        latency = current_time - sent_time

        print(latency)
        packet = {'seq':seq,'latency':latency}
        packets.append(packet)
    except:
        print ("e")


rospy.init_node('mqtt_msg_listener', anonymous=True)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("192.168.1.3", 1883, 60)
client.loop_start()

count1 = 0
while count1 < 300000000:
    count1+=1

client.loop_stop()

total_latency = 0
average_latency = 0
packet_loss = 0
sent_packet_count = 100
count2 = 0

for packet in packets:
    count2+=1
    total_latency += packet['latency']

average_latency = total_latency/sent_packet_count
packet_loss = sent_packet_count - count2

print ("AVERAGE LATENCY: ",average_latency)
print ("PACKET_LOSS: ", packet_loss)