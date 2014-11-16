morse_and_ros-moveit_example
============================

Example to move a simulated robot in [MORSE](http://morse-simulator.github.io) using [MoveIt](http://moveit.ros.org) package from [ROS](http://www.ros.org). You can see a video of the system working [here](http://youtu.be/NkPyGqfW1sA).

Process to execute the example:

1. Start 'roscore'.
2. Start morse by executing 'morse run my_simulation' when you are in 'iri_klwr_morse' directory.
3. 'roslaunch iri_klwr_bringup start_moveit_with_klwr_in_morse.launch' 
4. 'roslaunch iri_klwr_bringup start_rviz_for_planning.launch' 
 
This code was used on ROS [Hydro](http://wiki.ros.org/hydro) and MORSE [v1.2-11](https://github.com/morse-simulator/morse/blob/1.2/RELEASE_NOTES); and I expect that it works also on new versions of ROS and MORSE.
