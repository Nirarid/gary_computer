#!/usr/bin/env python
import rospy
import numpy as np
from playsound import playsound
from std_msgs.msg import Bool

class Meow():
    def __init__(self):
        rospy.on_shutdown(self.terminate)
        #Instantiate publisher and subscriber  
        print("Setting up node...")
        rospy.Subscriber("meow_sensor", Bool, self.sensor_msg_cb)
        print("Subscribers ok")
        print("Starting Node...")
        rate = rospy.Rate(1) #1Hz 
        print("Node initialized 1hz")
        #Initialize node variables
        self.sound = False
        #Publish indicated message
        while not rospy.is_shutdown():
            if(self.sound == True):
                rospy.loginfo("Hey!")
                rospy.loginfo("Out of seeds! GARY COME HOME D:")
                playsound("./catkin_ws/src/gary_computer/scripts/Gary_meows.mp3")
                self.sound = False
            rate.sleep()
    
    #Process received command from follower
    def sensor_msg_cb(self,msg):
        if(msg.data == True):
            self.sound = True
        else:
            self.sound = False
    
    #Process node shutdown (called when node is killed)
    def terminate(self):
        rospy.loginfo("Terminating node...")


#Main code
if __name__ == "__main__":
    rospy.init_node("sensor_meow",anonymous=True)
    #try:
    Meow()
    #except:
        #rospy.logfatal("sensor meow node died")
