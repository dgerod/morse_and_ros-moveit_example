# =======================================================================================
# helpers/adapters.py
# =======================================================================================

from . import morse_local_config as exp_settings
from morse.builder import Component
from morse.middleware.ros_request_manager import ros_service, ros_action
from morse.core.overlay import MorseOverlay
from morse.core.exceptions import MorseServiceError
from morse.middleware.ros import ROSPublisher, ROSPublisherTF, ROSSubscriber

# ----------------------------------------------------------------------------------------

def morse_to_ros_namespace( name ):
    return name.replace(".", "/")

# ----------------------------------------------------------------------------------------

class ros:

    # Topics - Publisher/Subscriber and more
    # --------------------------------------
    
    class Publisher(ROSPublisher):
        pass
    
    class Subscriber(ROSSubscriber):
        pass
    
    class TfBroadcaster(ROSPublisherTF):
        pass
       
    # Decorators
    # --------------------------------------
    
    service = ros_service
    action = ros_action 
        
    # Classes inherit from MorseOverlay 
    # --------------------------------------
    
    class Service(MorseOverlay):
        """
        A ROS service is created to export MORSE services through the overlay class.
        Therefore, the class exporting this services must inherit from this.
        """
        pass
    
    class Action(MorseOverlay):
        """
        A ROS action is created to export MORSE services through the overlay class.
        Therefore, the class exporting this services must inherit from this.
        """
        pass
    
# Registers  
# --------------------------------------
            
    class ServiceRegister:
        """
        This class attaches (registers) a MORSE service to a ROS service that exports it.
        """   
        _mw_location = exp_settings.mw_loc;     
        
        @staticmethod
        def register( component, service_class, name = "" ):
            service = ros.Service._mw_location + service_class
            component.add_overlay( "ros", service, namespace = name )

    class ActionRegister:
        pass
    
    class TopicRegister:
        """
        This class attaches (registers) a MORSE datastream to a ROS datastream that exports it.
        """   
        _mw_location = exp_settings.mw_loc;     
        
        @staticmethod
        def register( component, name = "" ):
            component.add_interface("ros", topic = name )
            
# ----------------------------------------------------------------------------------------

def register_ros_service( obj, name, service_class ):
    service_path = exp_settings.mw_loc + service_class
    obj.add_overlay("ros", service_path, namespace = name )

def register_ros_action( obj, name, action_class ):
    action_path = exp_settings.mw_loc + action_class
    obj.add_overlay("ros", action_path, namespace = name )
    
def register_ros_topic( obj, name, topic_class = None ):
    if topic_class is not None:
        topic_path = exp_settings.mw_loc + topic_class
        obj.add_stream("ros", topic_path, topic = name )
    else:
        topic_path = ""
        obj.add_stream("ros", topic = name )
    
# =======================================================================================
