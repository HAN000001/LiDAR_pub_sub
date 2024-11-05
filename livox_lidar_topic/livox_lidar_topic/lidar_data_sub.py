import rclpu
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import struct
import time

class LivoxLiDARPublisher(Node):
	def __init__(self, name):
		super().__init__(name)
		self.publisher = self.create_publisher(Laserscan, 'lidar_bag', 10)
		self.timer = self.create_timer(0.1, self.publish_lidar_data)
		
		self.lidar_data = LaserScan()
		self.lidar_data.header.frame_id = "Livox_LiDAR"
		
		
	# def publish_lidar_data(self):
        