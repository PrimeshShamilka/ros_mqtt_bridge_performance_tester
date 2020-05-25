#!/usr/bin/python

import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField

def talker():
    pub = rospy.Publisher('chatter', PointCloud2, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz - go through the loop 10 times in a second 
    
    # PointCloud2
    msg_to_publish = PointCloud2()

    # PointField
    point_field = PointField()

    # generate data 
    data = []
    for i in range (256):
        data.append(i)

    counter = 1
    while not rospy.is_shutdown():
        str_to_publish = "Message %d"% (counter)

        point_field.name = str_to_publish
        point_field.offset = 0
        point_field.datatype = 7
        point_field.count = 1

        # Header
        msg_to_publish.header.stamp = rospy.get_rostime()
        msg_to_publish.header.seq = counter

        msg_to_publish.height = 1
        msg_to_publish.width = 1
        msg_to_publish.fields = [point_field]
        msg_to_publish.is_bigendian = True
        msg_to_publish.point_step = 32
        msg_to_publish.row_step = 32

        # Data
        msg_to_publish.data = data
        msg_to_publish.is_dense = False

        rospy.loginfo(msg_to_publish)
        pub.publish(msg_to_publish)

        counter+=1
        if counter == 101:
            break
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
