from pdfminer.high_level import extract_text
import subprocess
import sys
import docx2txt
import re
import fnmatch
from pickle import TRUE
import PIL
from PIL import Image
import tkinter
from tkinter import MULTIPLE, messagebox
from tkinter import filedialog
import pytesseract
from pytesseract import pytesseract
import os
import textractplus as tp

# Define path to tessaract.exe (default location is defined below)
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Define path to image
path_to_images = filedialog.askopenfilename(multiple=True)  # saving path of the file location

#Iterate over each file_name in the folder
for file_name in path_to_images:
   
    
    path = r"{}".format(file_name)     # Changing path into String
    
    pdf = re.findall(".pdf", path)           # Checkin for PDF file
     
    docx = re.findall(".docx", path)          # Checking for Docx formated files
    
    doc = re.findall(".doc", path)             # Checking for Doc formated files
    
    if pdf:
        def extract_text_from_pdf(path):
            return extract_text(path)
        if __name__ == '__main__':
           text = extract_text_from_pdf(path)  # Extracted data from pdf files
           print(text)
    
    
    elif docx:
        text = tp.process(path)
        text=text.decode("utf-8")
        print(text)
        
    elif doc:
        text = tp.process(path)
        text=text.decode("utf-8")
        print(text)
    else:
      print("Enter file in correct formatt.")