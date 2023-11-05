from __future__ import print_function
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import cv2


#C:\Users\V4SWHVY\Desktop\python_barCode\cropped.jpg
pic_path = r"C:\Users\V4SWHVY\Desktop\python_barCode\rotate.png"
# preprocessing using opencv
im = cv2.imread(pic_path, cv2.IMREAD_GRAYSCALE)
ret, bw_im = cv2.threshold(im, 70, 255, cv2.THRESH_BINARY)
cv2.imwrite('barcode_opencv.jpg', im)
cv2.imwrite('barcode.jpg', bw_im)
# zbar
barcodes = decode(bw_im)
print(barcodes)

# Display barcode and QR code location  
# def display(im, decodedObjects):

#     # Loop over all decoded objects
#     for decodedObject in decodedObjects: 
#         points = decodedObject.polygon

#         # If the points do not form a quad, find convex hull
#         if len(points) > 4 : 
#             hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
#             hull = list(map(tuple, np.squeeze(hull)))
#         else : 
#             hull = points

#         # Number of points in the convex hull
#         n = len(hull)

#         # Draw the convext hull
#         for j in range(0,n):
#             cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

#     # Display results 
#     cv2.imshow("Results", im)
#     cv2.waitKey(0)

