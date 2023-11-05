import pdfbox

p=pdfbox.PDFBox()


def convert_pdf_to_img(filePath):
   images =  p.pdf_to_images(filePath,outputPrefix=r"C:\Users\V4SWHVY\Desktop\OCR\images\image")
   print(images)
    

if __name__ == "__main__":
    convert_pdf_to_img("C:\\Users\\V4SWHVY\\Desktop\\OCR\\input_files\\barCode_Invoicey.pdf")


