#!/usr/bin/env python
# filter.py
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError 
from dynamic_reconfigure.server import Server
from rgb_filter.cfg import RGBFilterConfig

