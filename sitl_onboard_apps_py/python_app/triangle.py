#!/usr/bin/env python

import time
from flyt_python import api

# Predefined side length for the triangle trajectory
side_length = 10

# Initialize the drone API
print("Initializing drone API...")
drone = api.navigation(timeout=120000)
time.sleep(3)

# Takeoff to 10 meters
print("Taking off to 10 meters...")
drone.take_off(10)
time.sleep(10)  # Wait for the drone to reach the desired height

# Define the triangle points
# An equilateral triangle's vertices relative to the starting point
triangle_points = [
    (side_length, 0),  # Move to the first vertex
    (-side_length / 2, (side_length * (3**0.5)) / 2),  # Move to the second vertex
    (-side_length / 2, -(side_length * (3**0.5)) / 2)  # Move to the third vertex
]

# Move in a triangle trajectory
print("Starting triangle trajectory...")
for index, (x, y) in enumerate(triangle_points):
    print("Moving to point {}: (x={}, y={})".format(index+1, x, y))
    drone.position_set(x, y, 0, relative=True)
    time.sleep(15)  # Wait for the drone to reach the point

# Land the drone
print("Landing the drone...")
drone.land()
time.sleep(10)  # Wait for the drone to land

# Disconnect the drone interface
print("Disconnecting the drone interface...")
drone.disconnect()
