#!/usr/bin/python3

import rclpy
from rclpy.node import Node

class DrawCircleNode(Node):

    def __init__(self):
        super.__init__("Draw Circle")
        self.get_logger().info("Draw circle Node started")


def main(args=None):
    rclpy.init(args=args)
    rclpy.shutdown()