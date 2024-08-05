from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2
import numpy as np
import streamlit as st 
from PIL import Image
import requests
import urllib.request
from pathlib import Path
import PIL
from io import BytesIO
import time



def object_detection_live():
    #st.title('PCB Defects Detection')

    # URL to fetch continuous images
    url = 'http://192.168.182.214/cam-hi.jpg'

    # Display the live stream
    image_placeholder = st.empty()  # Placeholder to update the image

    # Flag to track if the button is clicked
    button_clicked = False
    Rbutton_clicked = False


    # Create the button to process image
    
    Reference_button = st.button('Set Reference Image')
    process_button = st.button('Process Image')

    col1, col2 = st.columns(2)
    

    while True:

        with col1:
            if Reference_button:
                Rbutton_clicked = True
                Reference_button = False

            response = requests.get(url)
            Reference_image = Image.open(BytesIO(response.content))
            reference_img = cv2.cvtColor(np.array(Reference_image), cv2.COLOR_RGB2BGR)

            if Rbutton_clicked:
                st.image(Reference_image,caption='Reference Image')
                
                Rbutton_clicked = False
                time.sleep(2)
        
        with col2:
            if process_button:
                button_clicked = True
                process_button = False

            response = requests.get(url)
            image = Image.open(BytesIO(response.content))

            if button_clicked:
                #st.image(image)
                
                button_clicked = False
                time.sleep(2)

                source_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

                gray1 = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)
                gray2 = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
                    # Compute absolute difference between the two images
                difference = cv2.absdiff(gray1, gray2)
                    # Apply thresholding to highlight the differences
                _, thresholded = cv2.threshold(difference, 10, 255, cv2.THRESH_BINARY)
                    # Find contours of the differences
                contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    # Draw rectangles around the differing regions
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(reference_img, (x, y), (x + w, y + h), (255, 0, 0), 5)
                    
                st.image(reference_img, caption='Component Defects')
                st.write("dannan source")
                    
                
                
                time.sleep(5)
            





            else:
            # Display the image without processing
                image_placeholder.image(image, channels="RGB")

        # Add a small delay to control the frame rate
        time.sleep(0.001)  # 0.1 second delay 
                
                
object_detection_live()