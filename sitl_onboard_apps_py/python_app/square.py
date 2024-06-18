#!/usr/bin/env python

import time
from flyt_python import api

# Initialize the drone API
print("Initializing drone API...")
drone = api.navigation(timeout=120000)
time.sleep(3)

# Takeoff to 5 meters
print("Taking off to 5 meters...")
drone.take_off(5)
time.sleep(10)  # Wait for the drone to reach the desired height

# Predefined side length for the square trajectory
side_length = 6.5

# Move in a square trajectory of side length 6.5 meters at height 5 meters
print("Starting square trajectory...")
square_points = [
    (side_length, 0),   # Move to the first point
    (0, side_length),   # Move to the second point
    (-side_length, 0),  # Move to the third point
    (0, -side_length)   # Move to the starting point
]

for index, (x, y) in enumerate(square_points):
    print("Moving to point {}: (x={}, y={})".format(index + 1, x, y))
    drone.position_set(x, y, 0, relative=True)
    time.sleep(15)  # Wait for the drone to reach the point

# Land the drone
print("Landing the drone...")
drone.land()
time.sleep(10)  # Wait for the drone to land

# Disconnect the drone interface
print("Disconnecting the drone interface...")
drone.disconnect()
