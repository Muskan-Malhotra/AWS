from pdf_image import convert_pdf_to_img
from pdf_to_Image import pdf_2_img
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\V4SWHVY\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def text_extraction(filePath):
    convert_pdf_to_img(filePath)
    # convert_from_path(filePath)
    dir = "images"
    text = ""
    for filename in os.listdir(dir):
        f=os.path.join(dir,filename)
        text += pytesseract.image_to_string(f)
        print(text)
    return text
        # pytesseract.image_to_string()


if __name__ == "__main__":
    text_extraction(r"C:\Users\V4SWHVY\Desktop\OCR\input_files\BarCode1_2023_09_08_02_58_10.pdf")