#!/usr/bin/python

import rospy
from bridge_performance_tester.msg import custom_msg

def talker():
    pub = rospy.Publisher('chatter', custom_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1000000) # 10hz - go through the loop 10 times in a second 
    msg_to_publish = custom_msg()
    counter = 1

    while not rospy.is_shutdown():
        str_to_publish = "Message %d"% (counter)
        age_to_publish = counter
        flag_to_publish = True

        msg_to_publish.header.stamp = rospy.get_rostime()
        msg_to_publish.header.seq = counter
        msg_to_publish.name = str_to_publish
        msg_to_publish.age = age_to_publish
        msg_to_publish.flag = flag_to_publish

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
