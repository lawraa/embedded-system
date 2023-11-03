# Socket Server and Data Visualization
Create a program in stm32 to read the sensor value, such as 3D Accelerator and 3D gyro, and send the data to a Linux/Windows/Mac host and Visualize with some kind of GUI tools (such as using Python, https://mode.com/blog/python-data-visualization-libraries/ )

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Collaborators](#collaborators)

## Description
This repository contains two files: `main.cpp` and `socket-server.py`. `socket-server.py` acts as the server, listening to data from `main.cpp`, and plots the received data. The purpose of this project is to demonstrate data transfer between a C++ program and a Python server, with data visualization using Matplotlib.

## Installation
Ensure you have the required dependencies installed:
1. For socket-server.py:
- Python 3
- NumPy
- Matplotlib
2. For main.cpp:
- Mbed OS (make sure you have a compatible target)

## Collaborators

Partner that contributed to this project:
- **Shou-Jen, Chen**
- **Li-Chun, Lu**

