import os
# import poppler

from pdf2image import convert_from_path, convert_from_bytes

# from pdf2image.exceptions import (
#     PDFInfoNotInstalledError,
#     PDFPageCountError,
#     PDFSyntaxError
# )

poppler_path=r'C:\poppler\poppler-0.67.0\bin'


def pdf_2_img(filePath):
    images = convert_from_path(filePath, poppler_path=poppler_path)
    return images
    # dir = "img"
    # for i in range(len(images)):
   
    #   # Save pages as images in the pdf
    #     images[i].save(dir+'/'+'page'+ str(i+1) +'.jpg', 'JPEG')

if __name__ == "__main__":
    pdf_2_img("./input_files/Leave Policy.pdf")




#CMake must be installed to build the following extensions: poppler.cpp.modules: pip install cmake
#needed to install pip install python-poppler (Poppler)