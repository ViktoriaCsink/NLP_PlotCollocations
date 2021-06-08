# -*- coding: utf-8 -*-
"""
This function processes text from pdf files. 
Scanned pdfs are also supported.

@author: Viktoria
April, 2021

"""

#process pdfs if they are already downloaded into a folder

import pdfplumber
import ocrmypdf
import textract
import os
import magic

def read_pdf(title, directory):
    
    os.chdir(directory)
    
    #Only process if file is a pdf
    filetype = magic.from_file(title)
    
    if 'PDF' in filetype:
    
        with pdfplumber.open(title) as pdf:
            
            page = pdf.pages[0]
            text = page.extract_text()
        
            if text==None: #scanned pdf
                if __name__ == '__main__':
                    ocrmypdf.ocr(title, 'myfile_converted.pdf', deskew=True, progress_bar=False)
                    content = textract.process('myfile_converted.pdf', method='pdfminer') #pdf
                    os.remove('myfile_converted.pdf')
                                
            else:
                content = textract.process(title, method='pdfminer') #pdf
                
    else:
        content = None
    
    return content