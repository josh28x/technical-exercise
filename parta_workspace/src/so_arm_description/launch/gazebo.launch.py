#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Get the package directory
    package_dir = get_package_share_directory('so_arm_description')
    
    # Path to the URDF file
    urdf_path = os.path.join(
        get_package_share_directory('so_5dof_arm100_8j_urdf_sldasm'),
        'urdf',
        'so_5dof_arm100_8j_urdf_sldasm.urdf'
    )
    
    # Path to the world file
    world_path = os.path.join(
        get_package_share_directory('so_arm_description'),
        'worlds',
        'default.world'
    )
    
    # Check if the URDF file exists
    if not os.path.exists(urdf_path):
        raise FileNotFoundError(f"URDF file not found at {urdf_path}")
    
    # Launch Gazebo server with world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={
            'world': world_path,
            'extra_gazebo_args': ''
        }.items()
    )

    # Launch gzclient manually to ensure GUI opens
    gzclient = ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )

    # Spawn the robot into Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'so_arm',
            '-file', urdf_path,
            '-x', '0.0',
            '-y', '0.0',
            '-z', '1.0'
        ],
        output='screen',
    )
    
    # Static transform publisher
    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
        output='screen',
    )
    
    # Return the LaunchDescription
    return LaunchDescription([
        gazebo,
        gzclient,
        static_tf,
        spawn_entity,
    ])

