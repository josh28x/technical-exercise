#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Get the package directory
    package_dir = get_package_share_directory('so_arm_description')
    
    # Path to the URDF file
    urdf_path = '/home/joshua/Desktop/technical-exercise/parta_workspace/src/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf'
    
    # Path to the world file
    world_path = '/home/joshua/Desktop/technical-exercise/parta_workspace/src/so_arm_description/worlds/default.world'
    
    
    # Check if the URDF file exists
    if not os.path.exists(urdf_path):
        raise FileNotFoundError(f"URDF file not found at {urdf_path}")
    
    # Configure Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
    )
    
    # Spawn the robot
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'so_arm',
            '-file', urdf_path,
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.0'
        ],
        output='screen',
    )
    
    # Static Transform Publisher (replaces tf_footprint_base node from ROS1)
    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
        output='screen',
    )
    
    # Return the LaunchDescription
    return LaunchDescription([
        gazebo,
        static_tf,
        spawn_entity,
    ])
