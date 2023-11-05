from datetime import datetime
from logging import basicConfig,WARNING,error,warning
from urllib import parse
from os import path
from pathlib import Path
from vwits.iris.cv.services.text_extraction_service.text_extraction import text_extract

def text_extraction(file:str,case_id:str):
    """
    :param file : input file for processing.
    :case_id : case_id generated across filename.

    This function return bouding_box details and raw_text from documents.
    Insert returned data to  ocr_result collection and raw_text_output collection respectively.
    Update process_id in files collection 2 on success else -1.
    """
    
        
    bounding_box_result,raw_text_result=text_extract(file)

if __name__ == '__main__': 
    file="/home/ubuntu/ashutosh/research/inhouse_ocr/vwits/iris/cv/image_processing/data/image_archive/1638610501396_invoice.pdf"
    print(text_extraction(file,"123"))