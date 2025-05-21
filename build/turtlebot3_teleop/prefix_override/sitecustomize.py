import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ratkaba/workspace/src/ros2-traffic-project/install/turtlebot3_teleop'
