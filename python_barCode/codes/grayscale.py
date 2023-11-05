from PIL import Image #pillow
from pyzbar.pyzbar import decode #install pyzbar     
from glob import glob
from pyzbar.pyzbar import ZBarSymbol
import cv2
import numpy as np


# img = Image.open(r'C:\Users\V4SWHVY\Desktop\python_barCode\images\image3.jpg')

txtfiles = []
i=1
for file in glob(r"C:\Users\V4SWHVY\Desktop\python_barCode\images\image1.jpg"):
    image = cv2.imread(file)
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the Scharr gradient magnitude representation of the images
    # in both the x and y direction
    gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
    gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
    # construct a closing kernel and apply it to the thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations = 4)
    closed = cv2.dilate(closed, None, iterations = 4)
    # find the contours in the thresholded image, then sort the contours
    # by their area, keeping only the largest one
    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    txtfiles.append(kernel)


# for i in range(len(txtfiles)):
#     print(i)
#     if(txtfiles[i+1]<len(txtfiles)):
#         for j in range(txtfiles[i],txtfiles[i+1]):
#             print("move",j)
#     else:
        

# decoded_list = decode(img)
# print(decoded_list)
print(txtfiles)