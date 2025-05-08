from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node

def generate_launch_description():
    # Simplified parameters
    robot_description = {"robot_description": ""}  # Empty for now, we'll connect later
    controllers_path = "/home/joshua/Desktop/technical-exercise/parta_workspace/src/so_arm_description/config/controllers.yaml"
    
    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, controllers_path],
        output="both",
    )
    
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )
    
    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["so_arm_controller", "--controller-manager", "/controller_manager"],
    )
    
    # Delay start of robot_controller after joint_state_broadcaster
    delay_robot_controller_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[robot_controller_spawner],
        )
    )
    
    return LaunchDescription([
        control_node,
        joint_state_broadcaster_spawner,
        delay_robot_controller_spawner,
    ])
