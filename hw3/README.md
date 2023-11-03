# BLE Central Communication with Smart Phone Apps

This repository contains a Python program, `ble_scan_connect.py`, designed to communicate with a test Android app via BLE (Bluetooth Low Energy) from a Linux host, such as a Raspberry Pi 3. The program demonstrates some Client Characteristic Configuration Descriptor (CCCD) settings, including setting the CCCD value of your Android app to `0x0002` for indication and `0x0001` for notification.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Explanation](#explanation)
- [Collaborators](#Collaborators)


## Introduction

Bluetooth Low Energy (BLE) is a wireless communication technology widely used for connecting devices like smartphones, tablets, and embedded systems. This repository provides a Python program that acts as a BLE Central device (host) running on a Linux host, specifically a Raspberry Pi 3. The program communicates with a test Android/Iphone app, such as "LightBlue," to demonstrate CCCD settings and communication.

## Usage

1. Clone the repository to your Raspberry Pi 3 or Linux host:

   ```bash
   sudo apt install python3-pip
   sudo apt install libglib2.0-dev 
   sudo pip install bluepy

## Explanation
The ble_scan_connect.py program uses the bluepy library to interact with BLE devices. Here's an overview of what the program does:

- It scans for nearby BLE devices and lists them, allowing you to choose the device to connect to.
- After connecting, it retrieves services and characteristics from the BLE device.
- It reads the CCCD value and changes it to enable notifications.
- Finally, it waits for notifications from the device and prints them.

## Collaborators

Partner that contributed to this project:
- **Shou-Jen, Chen**
- **Li-Chun, Lu**
