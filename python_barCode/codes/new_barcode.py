from PIL import Image #pillow
from pyzbar.pyzbar import decode #install pyzbar     
from glob import glob
from pyzbar.pyzbar import ZBarSymbol
import cv2

path = r'C:\Users\V4SWHVY\Desktop\python_barCode\images\image10.jpg'
image = Image.open(r'C:\Users\V4SWHVY\Desktop\python_barCode\images\image1.jpg')

img = cv2.imread(path)
# # imS = cv2.resize(img, (960, 540))    
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# barcodes = decode(image)
# print(barcodes)

# for barcode in barcodes:
#     x,y,w,h = barcode.rect
#     cv2.rectangle(img,(x,y),(x+w,y+h),0,0,255,4)
#     bdata = barcode.data.decode("utf-8")
#     btype =  barcode.type
#     text = f"{bdata},{btype}"
#     cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

bd = cv2.barcode.BarcodeDetector()
# bd = cv2.barcode.BarcodeDetector()
# bd = cv2.barcode.BarcodeDetector('path/to/sr.prototxt', 'path/to/sr.caffemodel')

retval, decoded_info, decoded_type = bd.detectAndDecode(img)
print(retval)
# img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

# for s, p in zip(decoded_info, points):
#     img = cv2.putText(img, s, p[1].astype(int),
#                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

# cv2.imwrite('data/dst/barcode_opencv.jpg', img)

# txtfiles = []
# i=1
# for file in glob(r"C:\Users\V4SWHVY\Desktop\python_barCode\images\*.jpg"):
#     image = cv2.imread(file)
 
#     detectedBarcodes = decode(image)
    
#     for barcode in detectedBarcodes:
        
#         (x, y, w, h) = barcode.rect
#         cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
    
#         print(barcode.data)
#         txtfiles.append(i)
#         # print(barcode.type)
#     i += 1

# for i in range(len(txtfiles)):
#     print(i)
#     if(txtfiles[i+1]<len(txtfiles)):
#         for j in range(txtfiles[i],txtfiles[i+1]):
#             print("move",j)
#     else:
        

# decoded_list = decode(img)
# print(decoded_list)
# print(txtfiles)