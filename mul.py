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
#print(path_to_images)

for i in path_to_images:
#     #Iterate over each file_name in the folder
     img=r"{}".format(i)
     
#         #Open image with PIL
    #  print(img)
     text_data = pytesseract.image_to_string(img ,lang='eng')

     print(text_data)