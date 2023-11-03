# HW-1: Mbed OS Semaphore and Button/LED IO

This project is an introductory exercise to using semaphores and handling button and LED I/O on an STM32 IoT node with Mbed OS.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Mbed Studio IDE](https://os.mbed.com/studio/)
- [Mbed CLI](https://os.mbed.com/docs/mbed-os/v6.15/build-tools/mbed-cli.html) (Optional, if you prefer command-line tools)
- A supported Mbed-enabled board (e.g., STM32 IoT node)

### Installing

1. **Create Project**
   - Launch Mbed Studio IDE.
   - Create an `mbed-os-empty` project.
   - Rename the project to a name of your choice, appropriate to the assignment.

2. **Replace main.cpp**
   - Download the provided `main.cpp` from the assignment instructions.
   - Replace the `main.cpp` file in your project with the downloaded file.
   - You can modify the `main.cpp` as needed for your design.

3. **Compile and Test**
   - Compile the project within Mbed Studio IDE.
   - Connect your STM32 IoT node to your computer.
   - Test the compiled program by flashing it to the STM32 IoT node.

### Designing Your Own main.cpp

Your `main.cpp` should meet the following criteria:

1. **LED1 Blinking**
   - Initially, LED1 should blink with a period of 1 second.

2. **Button Press Handling**
   - When the USER BUTTON is pressed, LED1 should stop blinking.
   - Upon the button press, LED2 should start blinking with a period of 1 second.

## Additional Resources

- [Mbed OS Documentation](https://os.mbed.com/docs/)
- [InterruptIn API](https://os.mbed.com/docs/mbed-os/v6.15/apis/interruptin.html)

## Authors

- **Shou Jen, Chen**
- **Li Chun, Lu**
