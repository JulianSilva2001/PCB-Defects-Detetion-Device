from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2
import streamlit as st 
from PIL import Image
import urllib.request
import numpy as np
import PIL

def Component_Defects_upload():
    
    reference_img = st.sidebar.file_uploader(
            "Choose a reference PCB...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    if reference_img is not None:
        st.sidebar.image(reference_img)
    
    source_img = st.sidebar.file_uploader(
            "Choose a source PCB...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    if reference_img is not None and source_img is not None:
        reference_img = Image.open(reference_img)
        source_img = Image.open(source_img)
    

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                    st.write("no image uploaded")
            else:
                #uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                            use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
                st.write("no image uploaded")
                    
        else:
            if st.sidebar.button('Detect Objects'):                       
                reference_img = cv2.cvtColor(np.array(reference_img), cv2.COLOR_RGB2BGR)
                source_img = cv2.cvtColor(np.array(source_img), cv2.COLOR_RGB2BGR)

                # Convert images to grayscale
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
                
                st.image(reference_img, caption='Reference Image with Differences Detected')
            else:
                st.sidebar.write("Please upload both a reference image and a source image.")


