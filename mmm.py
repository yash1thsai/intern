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

# Define path to tessaract.exe (default location is defined below)
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Define path to image
path_to_images = filedialog.askopenfilename(multiple=True)
# saving path of the file location
for i in path_to_images:
    #     #Iterate over each file_name in the folder
    # Changing path into String
    path = r"{}".format(i)
    # Checkin for PDF
    img = re.findall(".pdf", path)
    if img:
        def extract_text_from_pdf(path):
            return extract_text(path)
        if __name__ == '__main__':
           text = extract_text_from_pdf(path)  # Extracted data from pdf files

    # Checking for Docx formated files
    img = re.findall(".docx", path)
    if img:
        def extract_text_from_docx(path):
            txt = docx2txt.process(path)
            if txt:
                return txt.replace('\t', ' ')
            return None
        if __name__ == '__main__':
           # Extracted text data from docx files
           text = extract_text_from_docx(path)
           print(text)