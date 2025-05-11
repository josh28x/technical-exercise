#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class ArmController(Node):
    def __init__(self):
        super().__init__('arm_controller')
        self.publisher = self.create_publisher(JointTrajectory, '/set_joint_trajectory', 10)
        self.wave()
    
    def wave(self):
        msg = JointTrajectory()
        msg.joint_names = ['Rotation', 'Pitch', 'Elbow', 'Wrist_Pitch', 'Wrist_Roll', 'Jaw']
        
        # Create a waving motion
        points = []
        
        # First position - arm down
        point1 = JointTrajectoryPoint()
        point1.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        point1.time_from_start = Duration(sec=1)
        points.append(point1)
        
        # Second position - arm raised
        point2 = JointTrajectoryPoint()
        point2.positions = [0.0, 0.5, 1.2, 0.0, 0.0, 0.0]  
        point2.time_from_start = Duration(sec=2)
        points.append(point2)
        
        # Third position - wave motion 1
        point3 = JointTrajectoryPoint()
        point3.positions = [0.0, 0.5, 1.2, 0.5, 0.0, 0.0]  
        point3.time_from_start = Duration(sec=3)
        points.append(point3)
        
        # Fourth position - wave motion 2
        point4 = JointTrajectoryPoint()
        point4.positions = [0.0, 0.5, 1.2, -0.5, 0.0, 0.0]  
        point4.time_from_start = Duration(sec=4)
        points.append(point4)
        
        msg.points = points
        self.publisher.publish(msg)
        self.get_logger().info('Published wave trajectory')

def main():
    rclpy.init()
    controller = ArmController()
    rclpy.spin_once(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
