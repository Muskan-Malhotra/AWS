import pdfplumber

with pdfplumber.open(r'C:\Users\V4SWHVY\Desktop\python_barCode\BarCode2.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text = page.extract_text()
        print(text)