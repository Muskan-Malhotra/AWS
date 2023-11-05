import easyocr
reader = easyocr.Reader(['en']) # need to run only once to load model into memory
result = reader.readtext(r'C:\Users\V4SWHVY\Desktop\python_barCode\image2.jpg')



print(result)

#Capture.PNG