# UAV Systems Engineer Assignment - FlytBase, Inc.

## Overview

This repository contains the assignment solutions for the UAV Systems Engineer role at FlytBase, Inc. The assignment includes creating two demo applications to control a drone using the FlytBase API in the FlytSIM simulator. The drone will execute predefined trajectories: a square and a triangle, followed by landing.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- A laptop with Ubuntu 16.04 or higher.
- Basic knowledge of Linux command line and C++/Python.
- FlytBase API documentation.
- FlytSIM simulator installed and configured.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SANTHOSH-MAMIDISETTI/Assignment.git
    ```
    ```bash
    cd Assignment
    ```

2. **Set up FlytSIM:**
   - Follow the FlytBase documentation to install and configure FlytSIM on your Ubuntu system.


## Usage

This repository contains two scripts: `square.py` and `triangle.py`.

### square.py

This script makes the drone take off to a height of 5 meters, move in a square trajectory with a side length of 6.5 meters, and then land.

1. **Run the script:**

    ```bash
    python square.py
    ```

2. **Output:**

    The drone will:
    - Take off to 5 meters.
    - Move to each corner of the square.
    - Land after completing the square trajectory.

### triangle.py

This script makes the drone take off to a height of 10 meters, move in a triangle trajectory with a side length of 10 meters, and then land.

1. **Run the script:**

    ```bash
    python triangle.py
    ```

2. **Output:**

    The drone will:
    - Take off to 10 meters.
    - Move to each vertex of the triangle.
    - Land after completing the triangle trajectory.

## Code Implementation Explanation

### square.py

1. **Initialization:**
    - The FlytBase API is initialized to set up a connection to the drone, allowing for communication and control of the drone's movements. The `timeout=120000` parameter ensures that the connection remains active for the duration of the task, providing ample time for the drone to complete its mission.

2. **Takeoff:**
    - The drone is commanded to take off to a height of 5 meters using the `take_off` method. This specific height is chosen to ensure the drone is high enough to avoid any ground-level obstacles during its flight. A 10-second delay is added to ensure the drone reaches the desired altitude before proceeding to the next commands.

3. **Square Trajectory:**
    - A square trajectory is defined with each side measuring 6.5 meters. The drone is directed to move to each corner of the square sequentially using the `position_set` method, which moves the drone to specific coordinates relative to its current position. This method simplifies the implementation by allowing incremental movements rather than absolute positioning, making the script more adaptable to different starting points.

4. **Landing:**
    - After completing the square trajectory, the drone is instructed to land using the `land` method. A delay ensures the drone has sufficient time to land safely. Finally, the `disconnect` method is called to close the connection to the drone, ensuring a clean and orderly shutdown of the control interface.

### triangle.py

1. **Initialization:**
    - Similar to `square.py`, the FlytBase API is initialized to establish a connection with the drone, with a 120-second timeout to ensure sufficient time for the drone to complete its task.

2. **Takeoff:**
    - The drone is commanded to take off to a height of 10 meters. This higher altitude is chosen to demonstrate the drone's capability to operate at different heights and to ensure clear airspace for the triangular trajectory. A 10-second delay is included to allow the drone to stabilize at the desired altitude.

3. **Triangle Trajectory:**
    - The script defines an equilateral triangle with each side measuring 10 meters. The vertices of the triangle are calculated based on standard geometric principles, ensuring precise movements. The `position_set` method is used to move the drone to each vertex of the triangle in sequence, with relative positioning simplifying the calculations and implementation.

4. **Landing:**
    - After completing the triangle trajectory, the drone is instructed to land. A delay ensures the drone has time to descend safely. The connection to the drone is then disconnected, ensuring a proper termination of the control session.

## Contributing

If you have suggestions for improving this repository, feel free to create an issue or submit a pull request.


## Contact

For any questions or feedback, please contact [mamidisettisanthosh2004@gmail.com](mailto:mamidisettisanthosh2004@gmail.com).
