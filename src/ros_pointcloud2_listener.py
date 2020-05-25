#!/usr/bin/env python

import rospy
import os
import time
from sensor_msgs.msg import PointCloud2
path = os.getcwd() + '/output_mqtt_simple.csv'

packets = []

def callback(data):
    
    global path
    global packets

    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

    sent_time = float(str(data.header.stamp.secs) + '.' + str(data.header.stamp.nsecs))
    ros_current_time = rospy.get_rostime()
    current_time = float(str(ros_current_time.secs) + '.' + str(ros_current_time.nsecs))
    latency = current_time - sent_time
    
    packet = {'seq':data.header.seq,'latency':latency}

    packets.append(packet)

    # output_logf = open(path, 'a')
    # now = rospy.get_rostime()
    # s = ""
    # s += data.name + ',' + str(data.header.seq) + ',' + str(data.header.stamp.secs) +'.' + str(data.header.stamp.nsecs) + ',' + str(now.secs) + '.' + str(now.nsecs) +'\n'
    # output_logf.write(s)
    # output_logf.close()

def listener():

    global path
    global packets

    # output_logf = open(path, 'w')
    # s = ""
    # s += 'data.name' + ',' + 'data.header.seq' + ',' + 'data.header.stamp'  + ',' + 'now.stamp' + '\n'
    # output_logf.write(s)
    # output_logf.close()

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/pong', PointCloud2, callback)

    # spin() simply keeps python from exiting until this node is stopped
    while not rospy.is_shutdown():
        rospy.spin()
        
    total_latency = 0
    average_latency = 0
    packet_loss = 0
    sent_packet_count = 100
    count = 0

    for packet in packets:
        count+=1
        total_latency += packet['latency']

    average_latency = total_latency/sent_packet_count
    packet_loss = sent_packet_count - count

    print ("AVERAGE LATENCY: ",average_latency)
    print ("PACKET_LOSS: ", packet_loss)

if __name__ == '__main__':
    listener()
