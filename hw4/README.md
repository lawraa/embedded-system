# HW-4: Mbed BLE Programming - Peripheral and Central Integration

This homework project involves creating a BLE peripheral service with an Mbed OS supported STM32 board (e.g., DISCO-L475VG-IOT01A) that provides magnetometer and heart rate data, and a central device program running on a Raspberry Pi that receives and processes this BLE data. The system uses the MBED platform and is intended for the STM32L475 IoT node.

## Overview

Required to use of the EventQueue in managing BLE events, and the integration of sensor data into BLE services. Additionally, they will write a central device program that can interface with the peripheral to receive data over BLE.

### Goals

- Understand and modify the `BLE_GattServer_AddService` project to add new services.
- Develop an understanding of how BLE events are managed in Mbed OS.
- Implement a BLE peripheral service that transmits magnetometer and heart rate data.
- Write a central device program on Raspberry Pi to scan and receive data from the BLE peripheral.

## Prerequisites

- [Mbed OS](https://os.mbed.com/mbed-os/)
- [Python](https://www.python.org/) (for the Raspberry Pi central program)
- BLE-supported STM32 board (e.g., DISCO-L475VG-IOT01A)
- Raspberry Pi with BLE capabilities

## Main Features

### Heart Rate Service

- The heart rate service updates its value every second in a simulated fashion.
- It uses the standard Heart Rate Service UUID for BLE services.

### Magnetometer Service

- The magnetometer service updates the X, Y, and Z axis values upon each sensor value update call.
- It includes a custom service and characteristic UUID as per the BLE GATT specifications.

### BLE Advertising

- The device advertises itself as "Heartrate_team5" and includes the UUIDs for the Heart Rate and Magnetometer services in the advertisement packet.
- Advertising is restarted upon disconnection to allow new clients to connect.

## Dependencies

- MBED OS
- MBED BLE API
- STM32L475 IoT node specific libraries (for magnetometer sensor)

## Building and Running

- Instructions on how to compile and deploy the application to the target hardware.

## Usage with Raspberry Pi

- The `ble_raspi.py` script is a BLE client that can be used to connect and subscribe to the BLE services advertised by the application.
- The script requires the `bluepy` library to be installed on the Raspberry Pi.
- Instructions on how to run the script and interact with the BLE services.

## Authors

- **Li Chun, Lu**
- **Shou-Jen, Chen**

