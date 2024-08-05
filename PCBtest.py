from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2
import streamlit as st 
from PIL import Image
import urllib.request

model = YOLO('best (1).pt') 
url= 'http://192.168.182.214/cam-hi.jpg'
#img= cv2.imread('test6.jpg')

st.title('PCB Defects Detection')
#image=st.file_uploader('upload image' , type=['png', 'jpg', 'jpeg','gif'])
#image=urllib.request.urlopen(url)

# Load two images
image1 = cv2.imread('short.jpg')
image2 = cv2.imread('AnomTest4.png')
# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# Compute absolute difference between the two images
difference = cv2.absdiff(gray1, gray2)
# Apply thresholding to highlight the differences
_, thresholded = cv2.threshold(difference, 50, 255, cv2.THRESH_BINARY)
# Find contours of the differences
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw rectangles around the differing regions
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image1, (x, y), (x + w, y + h), (255, 0, 0), 5)
# Display the result
#cv2.imshow('Difference', image1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



st.sidebar.image(image1)
    



#model.predict(source="0", show= True , conf=0.9)

#results = model(['test1.jpg', 'test2.jpg'])  # return a list of Results objects
#model.predict('test6.jpg', save=True, conf=0.3)

# Process results list





#print(result)


