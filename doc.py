import re
import os
import sys
import win32com.client as win32
from win32com.client import constants
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
from glob import glob
import win32com.client as win32
from win32com.client import constants
import textractplus as tp

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
  file_path = r"{}".format(i)
  text = tp.process(file_path)
  print(text)