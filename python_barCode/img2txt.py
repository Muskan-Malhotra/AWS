import easyocr


def imgText(imagePath):
    collect = []
    reader = easyocr.Reader(['en']) # need to run only once to load model into memory
    result = reader.readtext(imagePath)
    for i in result:
        collect.append(i[-2])

    idx = int(len(collect)/2)

    for i in range(len(collect),idx,-1):
        # print(i[-2])
        res = list(filter(lambda x: 'AP523' in x, collect))
        return res   
    
    return res

#Capture.PNG

if __name__=="__main__":
    val = imgText(r'C:\Users\V4SWHVY\Desktop\python_barCode\img_test\rotate.PNG')
    print(val)
    #C:\Users\V4SWHVY\Desktop\python_barCode\img_test\rotate.PNG