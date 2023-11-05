import os
import pathlib



filePath = os.path.basename(r"C:\Users\V4SWHVY\Desktop\Leave Policy.pdf")
# print(pathlib.Path(filePath))

fileName = os.path.splitext(filePath)[0]
fileExt = os.path.splitext(filePath)[1]
split_file1 = os.path.basename(filePath)
print(split_file1)