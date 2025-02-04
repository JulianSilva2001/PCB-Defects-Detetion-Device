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

## PCB and Schematic Design

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

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Shematic.png)
*Figure 1: Schematic Diagram*

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/PCB1.png)
![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/PCB2.png)
*Figure 2: PCB Design*




## Enclosure Design 

### 🏗 Key Considerations
The enclosure was designed to optimize functionality, ease of use, and performance:

1. **Mounting for Camera and PCB**
   - Dedicated mounting points secure the camera and PCB for stable inspection.
   
2. **Acrylic Flat Surface**
   - Provides a clear, stable platform for precise PCB inspection.

3. **Adjustable Camera Height**
   - An aluminum bar allows users to set the optimal distance for capturing detailed images.

4. **Ring of Light**
   - Ensures uniform illumination, eliminating shadows for accurate defect detection.

5. **On/Off Button**
   - Controls the power supply, enhancing convenience and safety.

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Enclosure1.png)
*Figure 3: Enclosure V1*

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Enclosure2.png)
*Figure 4: Enclosure V2*

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Enclosure%20Draft%20Analysis.png)

*Figure 5: Draft Analysis*

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Image%20Doc/PCBfitsEnclosure.jpg)
*Figure 6: How the PCB fits the enclosure*

## 🌐 Building the Web Application

### 📂 Application Structure
The web app offers real-time PCB defect detection through a live camera feed or image uploads.

### 🏠 Home Page
Displays a **welcome message** and describes the types of defects detected:
- Missing Hole
- Mouse Bite
- Open Circuit
- Short Circuit
- Spur
- Spurious Copper

Users can choose between **Live Inspection** or **Upload Images**.


![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/CoverPage.png)
*Figure 7: Cover Page*

### 📑 Sidebar Menu
Provides navigation options:
- **About**
- **PCB Defects**
- **Component Defects**

### 🖼 PCB Defects Page
#### ⚙ Model Configuration
Users can:
- Select **Live Camera** or **Upload PCB Image**.
- Adjust model confidence using a slider.

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/PCBdefects_upload.png)
*Figure 8: PCB defects Detection Page* 

#### 🎥 Live Camera Mode
- Captures real-time images.
- Detects defects using the YOLO model.
- Highlights defects on the processed image.

#### 📤 Upload PCB Image Mode
- Users upload PCB images in various formats.
- The app processes and highlights detected defects.

### 🔩 Component Defects Page
Similar to PCB defects detection, but focuses on **component placement**.

![PCB](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/Component%20Placement%20Inspection%20.png)
*Figure 8: Component Placement Inspection Page* 

#### 🎥 Live Camera Mode
- Captures a reference image.
- Compares it with live images to detect misalignments.

#### 📤 Upload PCB Image Mode
- Users upload a **reference** and **source image**.
- The app highlights component defects based on differences.

## Getting Started

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/yourusername/pcb-defects-detection-device.git
    ```


2. **Running the Device**: Follow the setup instructions in the documentation to assemble the hardware and run the device.

## Documentation

Detailed documentation, including setup instructions and usage guidelines, can be found in the [project document](https://github.com/JulianSilva2001/PCB-Defects-Detetion-Device/blob/main/Documentation/PCB_Defects_Detection_Documentation%20(7).pdf).

