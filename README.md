morse_and_ros-moveit_example
============================

Move a simulated robot in MORSE [http://morse-simulator.github.io] using MoveIt package [http://moveit.ros.org/] from ROS [http://www.ros.org/].

Process to execute the example:
1. Start 'roscore'.
2. Start morse by executing 'morse run my_simulation' when you are in 'iri_klwr_morse' directory.
3. 'roslaunch iri_klwr_bringup start_moveit_with_klwr_in_morse.launch' 
4. 'roslaunch iri_klwr_bringup start_rviz_for_planning.launch' 
