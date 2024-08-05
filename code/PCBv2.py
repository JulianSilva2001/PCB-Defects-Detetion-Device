from ultralytics import YOLO
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import time
import urllib.request


model = YOLO('best (1).pt')
confidence=0.2
# Placeholder function for image processing
def process_image():
    
    url = 'http://192.168.182.214/cam-hi.jpg'
    image=urllib.request.urlopen(url)
    image = Image.open(image)
    #st.image(image=image)
    #result= model(image)
    #names = result[0].names
    #probability = result[0].probs
   
    res = model.predict(image,conf=confidence)
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]
    st.image(res_plotted, caption='Detected Image',use_column_width=True)


    # Perform your image processing here using your YOLO model
    # Replace this placeholder with your actual image processing code
    #result = image  # Placeholder for the result
    return 

# Main Streamlit app
def main():
    st.title('PCB Defects Detection')

    # URL to fetch continuous images
    url = 'http://192.168.182.214/cam-hi.jpg'

    # Display the live stream
    image_placeholder = st.empty()  # Placeholder to update the image

    # Flag to track if the button is clicked
    button_clicked = False

    # Create the button to process image
    process_button = st.button('Process Image')

    while True:
        # If the button is clicked, process the image
        if process_button:
            # Set the flag to True to indicate that the button is clicked
            button_clicked = True

            # Reset the button so it's not clicked again in the next iteration
            process_button = False

        # Fetch image from the URL
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

        if button_clicked:
            process_image()
            # Process the image if the button is clicked
            #processed_image = process_image(np.array(image))

            # Display the processed image
            #image_placeholder.image(processed_image, channels="RGB")
            
            button_clicked = False
            time.sleep(2)

              # Streamlit expects RGB format
        else:
            # Display the image without processing
            image_placeholder.image(image, channels="RGB")

        # Add a small delay to control the frame rate
        time.sleep(0.001)  # 0.1 second delay

if __name__ == '__main__':
    main()
