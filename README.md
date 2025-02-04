# PCB Defects Detection Device

This repository contains the code and resources for a PCB defects detection device. The project utilizes computer vision techniques and machine learning models to identify and classify defects in printed circuit boards (PCBs). 

## Overview

The PCB defects detection device is designed to automate the inspection process, ensuring high-quality standards in PCB manufacturing. The device employs a camera to capture images of PCBs and uses a trained model to detect various types of defects.

## Features

- *Defect Detection:* Identifies multiple PCB defects using a trained YOLOv8 model.
- *Component Placement Verification:* Compares PCB images to detect misaligned or missing components.


![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Image%20Doc/enclosurewithLap.jpg)

- **Computer Vision**: The project uses computer vision to process and analyze images of PCBs. This involves techniques such as image enhancement, feature matching, image transformation,  feature extraction, and object detection.
- **Model Training**: A machine learning model is trained on a dataset of PCB images with labeled defects. The model learns to identify and classify defects based on patterns in the images.
- **PCB Schematic and Design**: The repository includes the PCB schematic and design files, providing a comprehensive guide to the hardware setup.
- **Enclosure Design**: Design files for the device enclosure are also included, ensuring a complete package for building the physical device.
- **Web App**: The code for the web application used to interact with the device is also available, allowing for real-time monitoring and analysis through a user-friendly interface.

## PCB Schematic Design

### 🔩 Component Selection
The PCB inspection device consists of the following key modules:
1. **Microcontroller:** ESP-WROOM-32 (ESP32)
2. **Camera:** OV2460
3. **Lighting System:** High-brightness LED strip
4. **Power Supply:** Micro USB-powered regulated system

### 🔌 Microcontroller: ESP-WROOM-32
The ESP32S is chosen for its:
- **WiFi and Bluetooth Integration:** Enables high-speed image transmission (~6 Mbps).
- **Processing Power:** Dual-core Tensilica LX6 (240 MHz) for efficient image processing.
- **Memory:** 520 KB SRAM to support high-performance operations.

### 📷 Camera: OV5640
- **Resolution:** 5MP sensor 
- **Optical Features:** Low light sensitivity and high dynamic range for accurate PCB inspection.
- **Digital Video Port (DVP) Interface:** Ensures seamless integration with ESP32.
- **Power Requirements:** 2.8V core operation, 1.2V I/O.

### 🔋 Power Supply
- **Voltage Regulation:** Converts 5V USB input to required voltages.
- **Stable Power:** Voltage regulators ensure consistent performance.
- **Convenience:** USB-powered for easy deployment.

### 💡 Lighting System
- **LED Strip:** Provides uniform illumination for defect detection.
- **Adjustable Intensity:** Controlled via a potentiometer for adaptable lighting conditions.
- **Enhanced Versatility:** Ensures accurate inspection across diverse environments.



## Getting Started

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/yourusername/pcb-defects-detection-device.git
    ```


2. **Running the Device**: Follow the setup instructions in the documentation to assemble the hardware and run the device.

## Documentation

Detailed documentation, including setup instructions and usage guidelines, can be found in the [project document](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/PCB_Defects_Detection_Documentation%20(7).pdf).

