# import the Python Image
# processing Library
from PIL import Image
from glob import glob
from img2txt import imgText
from os import rename


path = "C:\\Users\\V4SWHVY\\Desktop\\python_barCode\\img_test\\"
#r"C:\Users\V4SWHVY\Desktop\python_barCode\img_test\*.PNG"

for file in glob(r'C:\Users\V4SWHVY\Desktop\python_barCode\images\*jpg'):

    # file = r"C:\Users\V4SWHVY\Desktop\python_barCode\img_test\image1.jpg"
    # Giving The Original image Directory
    # Specified
    print(file)
    Original_Image = Image.open(file)
    val1 = imgText(file)
    print(val1)

    # Rotate Image By 180 Degree
    rotated_image1 = Original_Image.transpose(Image.ROTATE_90)  # for left rotation

    # This is Alternative Syntax To Rotate
    # The Image
    # rotated_image2 = Original_Image.transpose(Image.TRANSPOSE)
    rotated_image2 = Original_Image.transpose(Image.ROTATE_270)  # in case of most invoices

    # for flip bottom to top
    # rotated_image3 = rotated_image2.transpose(Image.FLIP_LEFT_RIGHT)
    flip_top = rotated_image2.transpose(Image.FLIP_TOP_BOTTOM)
    rotated_image3 = flip_top.transpose(Image.FLIP_LEFT_RIGHT)



    # rotated_image1.save(rename('img.jpg','img1.jpg'))
    # rotated_image2.show()
    # flip_top.show()
    # rotated_image3.show()