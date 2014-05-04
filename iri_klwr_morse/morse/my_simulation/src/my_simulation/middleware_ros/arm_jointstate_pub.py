import logging; logger = logging.getLogger("morse."+ __name__)

from my_simulation.helpers import adapters

import roslib
import rospy
from sensor_msgs.msg import JointState

class JointStatePublisher(adapters.ros.Publisher):
    """ Publishes a JointState topic and set kuka_{1-7} to the position[0-6]. """
    ros_class = JointState

    def default(self, ci='unused'):
        
        message = JointState()        
        message.header = self.get_ros_header()      
        
        message.name = [''] * 7
        message.position = [0] * 7
        message.velocity = [0] * 7
        message.effort = [0] * 7
        
        # Define name used to export joints
        base_name = "kuka_joint_"
        
        for i in range(7):
            message.name[i] = base_name + ("%d" % (i+1) )
            message.position[i] = self.data[ "kuka_" + ("%d" % (i+1) ) ]

        self.publish(message)
