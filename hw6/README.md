# HW-6: Mbed BLE Programming - Peripheral and Central Integration

This homework project involves creating a BLE peripheral service with an Mbed OS supported STM32 board (e.g., DISCO-L475VG-IOT01A) that provides magnetometer and heart rate data, and a central device program running on a Raspberry Pi that receives and processes this BLE data. The system uses the MBED platform and is intended for the STM32L475 IoT node.

## Task Overview

1. We provide an example code in “timer_trigger_adc” folder to setup ADC triggered by timer, sampling the signal of STM32 internal temperature sensor at a fixed frequency and generating an interrupt when each conversion finishes. Please modify the (a) trigger frequency and (b) sampling time of ADC.

2. We provide an example code in “timer_trigger_adc_DMA_ver” folder to setup ADC triggered by timer, sampling the signal of STM32 internal temperature sensor at a fixed frequency. Further, the code setups DMA to transfer the data from ADC data register to a specific buffer when each conversion finishes. When the top half of buffer is filled, the interrupt will be generated and print all data in the top half of buffer. When the bottom half of buffer is filled, the interrupt makes all data in the bottom half of buffer printed. Finish the "TODO"

3. Here is an MbedOS microphone example which can record the sound in two second(https://github.com/janjongboom/b-l475e-iot01a-audio-mbed連結到外部網站。). Please modify the code such that the program executes continuously and periodically (You don’t need to preserve audio data or print it out). This code setups DMA to transfer audio data to PCM_Buffer. When the top and bottom half of PCM_Buffer are filled, the corresponding interrupts will generate. Please choose two GPIO pins as output and connect them to logic analyzer. Once the PCM_Buffer top half event occurs, toggle pin1’s output voltage. Once the PCM_Buffer bottom half event occurs, toggle pin2’s output voltage. By this way, you can observe the frequency of audio sampling.

## Files
**main-p1.cpp**: This file setup ADC triggers by timer and samples signal of STM32. We modify the trigger frequency and sampling time of ADC whihc is in `Line 165 and 167` and `Line 110` correspondingly. Our results/analysis are listed in our report that we submitted.

**main-p2.cpp**: This file provides example code that setups ADC triggered by timer. We implemented when top half of buffer is filled, the interrupt will be generated and print all data in the top half of buffer. Our results/analysis are listed in our report that we submitted.

**main-p3.cpp**: This file implemented a voltage change when the buffer reached top half and bottom half, and we examined the frequency of audio sampling in Logic Analyzer. `stm32l475e_iot01_audio.c` and `stm32l475e_iot01_audio.h` are files required for this main.cpp. 

## Authors

- **Li Chun, Lu**
- **Shou-Jen, Chen**
