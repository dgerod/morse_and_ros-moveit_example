import logging; logger = logging.getLogger("morse."+ __name__)

from my_simulation.helpers import adapters

import roslib;
import rospy
from control_msgs.msg import FollowJointTrajectoryAction

from morse.core.services import interruptible
from morse.core import status
from morse.core.exceptions import MorseServiceError

class ArmControllerByActions(adapters.ros.Service):
    """
    This overlay provides a ROS JointTrajectoryAction amd FollowJointTrajectoryAction 
    interfaces to armatures.
    Besides the ROS action server, it also sets a ROS parameter with the list of
    joints.
    """

    def __init__(self, overlaid_object, namespace = None):
        # Call the constructor of the parent class
        super(self.__class__,self).__init__(overlaid_object)

        joints = list(overlaid_object.local_data.keys())

        self.namespace = namespace
        name = adapters.morse_to_ros_namespace( self.name() )

        # ---
        
        #base_name = "iri_kuka_joint_"
        
        #joints = []
        #for i in range(7):
        #  joint_name = base_name + ("%d" % (i+1) )
        #  joints.append( joint_name )
        
        rospy.set_param(name + "/joint_names", joints)

    def _stamp_to_secs(self, stamp):
        return stamp.secs + stamp.nsecs / 1e9

    def name(self):

        if self.namespace:
            return self.namespace
        else:
            return super(self.__class__, self).name()

    # Export action for ROS
    # ------------------------------------------------------

    def follow_joint_trajectory_result(self, result):
        return result
    
    # The name of the 'action' in ROS is based on the name of this function.
        
    @interruptible
    @adapters.ros.action(type = FollowJointTrajectoryAction)
    def follow_joint_trajectory(self, req):
        """ Fill a MORSE trajectory structure from ROS JointTrajectory
        """

        traj = {}
        req = req.trajectory
        
        traj["starttime"] = self._stamp_to_secs(req.header.stamp)

        # Read joint names in message        
        joint_names = req.joint_names
        logger.info( req.joint_names )
                
        # Overwrite joint names from message to match ones defined by MORSE        
        for i in range( len(joint_names) ):
          joint_names[i] = joint_names[i].replace("kuka_joint", "kuka")        
        logger.info( joint_names )
        
        # Read positions from message
        target_joints = self.overlaid_object.local_data.keys()
        logger.info( target_joints )
        
        # Check if trajectory is correct or not
        diff = set(joint_names).difference(set(target_joints))
        if diff:
            raise MorseServiceError("Trajectory contains unknown joints! %s" % diff)

        points = []
        for p in req.points:
            point = {}

            # Re-order joint values to match the local_data order

            pos = dict(zip(joint_names, p.positions))
            point["positions"] = [pos[j] for j in target_joints if j in pos]
            vel = dict(zip(joint_names, p.velocities))
            point["velocities"] = [vel[j] for j in target_joints if j in vel]

            acc = dict(zip(joint_names, p.accelerations))
            point["accelerations"] = [acc[j] for j in target_joints if j in acc]

            point["time_from_start"] = self._stamp_to_secs(p.time_from_start)
            points.append(point)

        traj["points"] = points
        logger.info(traj)
        
        self.overlaid_object.trajectory(
                self.chain_callback(self.follow_joint_trajectory_result),
                traj)
