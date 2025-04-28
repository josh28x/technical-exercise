from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(
                '/home/joshua/Desktop/ros2_ws/src/so100_robot/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf', 'rb').read().decode('utf-8')}]
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'so100_robot', '-topic', 'robot_description'],
            output='screen'
        )
    ])


