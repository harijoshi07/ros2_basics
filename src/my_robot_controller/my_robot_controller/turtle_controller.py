#!/bin/usr/python3

import rclpy
from rclpy.node import Node

class TurtleControllerNode(Node):
    def __init__(self):
        super.__init__("turtle_controller")
        self.get_logger().info("Turtle controller started")


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(TurtleControllerNode())        #call node class here
    rclpy.shutdown()