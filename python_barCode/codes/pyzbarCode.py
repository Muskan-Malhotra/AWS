from PIL import Image
from pyzbar.pyzbar import decode
import glob
import cv2

data = decode(Image.open(r'C:\Users\V4SWHVY\Desktop\python_barCode\image1.jpg'))
print(data)

def read_qr_code(filename):
    """Read an image and read the QR code.
    
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """
    
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value, points, straight_qrcode
    except:
        return

value,a,b = read_qr_code(r'C:\Users\V4SWHVY\Desktop\python_barCode\Capture.PNG')
print(value,a,b)