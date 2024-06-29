#!/bin/usr/python3

import rclpy
from rclpy.node import Node



def main(args=None):
    rclpy.init(args=args)
    rclpy.spin()        #call node class here
    rclpy.shutdown()