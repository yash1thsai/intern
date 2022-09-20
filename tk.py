import tkinter
from PIL import Image
from pytesseract import pytesseract
from tkinter import filedialog
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir


file_path_variable = search_for_file_path()
print ("\nfile_path_variable = ", file_path_variable )


#Define path to image
path_to_images = file_path_variable

print(path_to_images)

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file_name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = Image.open(path_to_images +'/'+ file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img)

        print(text)



