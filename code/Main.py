# Python In-built packages

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

# External packages
#import streamlit as st

# Local Modules
#import settings
#import helper


# Setting page layout

confidence= 0.3
model = YOLO('best (1).pt')

st.set_page_config(
    page_title="PCB Inspection ",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
def main():
    new_title = '<p style="font-size: 42px;">Welcome to PCB Inspector!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)

    read_me = st.markdown("""
    TThis application helps you identify defects in your printed circuit boards (PCBs). It can detect various types of defects, including:

    Missing Hole: Detection of missing holes in the PCB.
    Mouse Bite: Identification of mouse bites on the PCB surface.
    Open Circuit: Detection of open circuits within the PCB traces.
    Short Circuit: Identification of short circuits between traces.
    Spur: Detection of spurious traces or anomalies.
    Spurious Copper: Identification of excess or misplaced copper traces.
    Additionally, the application can identify defects related to components, such as missing or incorrectly oriented components.

    You have two options for inspection:

    Live Inspection: Perform real-time inspection of a live PCB feed.
    Upload Images: Upload images of your PCBs to identify defects.
        
        
        Choose your preference from the sidebar menu to get started"""
    )
    st.sidebar.title("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("About","PCB Defects","Component Defects"))
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
        
    if choice == "PCB Defects":
        #st.subheader("PCB Defects")
        read_me_0.empty()
        read_me.empty()
            #st.title('Object Detection')
        object_detection_image()
    elif choice == "Component Defects":
        read_me_0.empty()
        read_me.empty()
            #object_detection_video.has_beenCalled = False
        #object_detection_video()
        Component_Defects()
        

    elif choice == "About":
        print()
    # Main page heading

  
def object_detection_image():
    global confidence
    st.title("PCB Defects Detection")
    st.subheader("PCB Defects")


    # Sidebar
    st.sidebar.header("ML Model Config")

    # Model Options
    model_type = st.sidebar.radio(
        "Select Task", ['Live Camera', 'Upload PCB Image'])

    confidence = float(st.sidebar.slider(
        "Select Model Confidence", 25, 100, 40)) / 100

    # Selecting Detection Or Segmentation

    model=YOLO('best (1).pt') 


    st.sidebar.header("Image/Video Config")

    source_img = None
    # If image is selected

    if model_type == 'Live Camera':
         object_detection_live()
    
    else:
        object_detection_upload()

def Component_Defects():
    st.title('Component Placement Inspection')

    model_type = st.sidebar.radio(
        "Select Task", ['Live Camera', 'Upload PCB Image'])

    if model_type == 'Live Camera':
         Component_Defects_live()
    
    else:
        Component_Defects_upload()



def process_image():
    model = YOLO('best (1).pt')
    
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

def object_detection_live():
    #st.title('PCB Defects Detection')

    # URL to fetch continuous images
    url = 'http://192.168.182.214/cam-hi.jpg'
    image_placeholder = st.empty()  # Placeholder to update the image
    button_clicked = False

    # Create the button to process image
    process_button = st.button('Process Image')

    while True:
        # If the button is clicked, process the image
        if process_button:
            button_clicked = True
            process_button = False

        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

        if button_clicked:
            process_image()
            
            button_clicked = False
            time.sleep(2)

        else:
            # Display the image without processing
            image_placeholder.image(image, channels="RGB")

        # Add a small delay to control the frame rate
        time.sleep(0.001)  # 0.1 second delay 


def get_index_by_value(value):
    for key, val in model.names.items():
        if val == value:
            return key
    # If the value is not found, return None or any other indication as per your requirement
    return None

def object_detection_upload():
    source_img = st.sidebar.file_uploader(
            "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    
    all_types = ['falsecopper','opencircuit','pinhole','scratch','shortcircuit','spur', 'missinghole', 'mousebite']
    selected_types = st.multiselect("Select types to predict", all_types)

    selected_indices = [get_index_by_value(type) for type in selected_types]


    st.text(selected_indices)

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                    st.write("no image uploaded")
            else:
                uploaded_image = PIL.Image.open(source_img)
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
                res = model.predict(uploaded_image,classes= selected_indices)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                                use_column_width=True) 

def Component_Defects_upload():
    st.subheader('Upload Image')
    
    reference_img = st.sidebar.file_uploader(
            "Choose a reference PCB...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    
    source_img = st.sidebar.file_uploader(
            "Choose a source PCB...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    if source_img is not None:
        st.sidebar.image(source_img)

    if reference_img is not None and source_img is not None:
        reference_img = Image.open(reference_img)
        source_img = Image.open(source_img)
    

    col1, col2 = st.columns(2)

    with col1:
        try:
            if reference_img is None:
                    st.write("No Reference PCB uploaded")
            else:
                #uploaded_image = PIL.Image.open(source_img)
                st.image(reference_img, caption="Reference PCB",
                            use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
                st.write("No testing PCB uploaded")
                    
        else:
            if st.sidebar.button('Test PCB'):                       
                reference_img = cv2.cvtColor(np.array(reference_img), cv2.COLOR_RGB2BGR)
                source_img = cv2.cvtColor(np.array(source_img), cv2.COLOR_RGB2BGR)

                # Convert images to grayscale
                gray1 = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)
                gray2 = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
                # Compute absolute difference between the two images
                difference = cv2.absdiff(gray2, gray1)
                # Apply thresholding to highlight the differences
                _, thresholded = cv2.threshold(difference, 110, 255, cv2.THRESH_BINARY)
                # Find contours of the differences
                contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # Draw rectangles around the differing regions
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    source_img = cv2.cvtColor(np.array(source_img), cv2.COLOR_BGR2RGB)
                    cv2.rectangle(source_img, (x, y), (x + w, y + h), (255, 0, 0), 5)

            
                st.image(source_img, caption='Tested PCB')
            else:
                st.sidebar.write("Please upload both a reference image and a source image.")

def Component_Defects_live():

    st.subheader('Live')
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



if __name__ == '__main__':
		main()	