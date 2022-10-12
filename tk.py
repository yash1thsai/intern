from pdfminer.high_level import extract_text
import subprocess
import sys
import docx2txt
import re
import fnmatch
from pickle import TRUE
import tkinter
from tkinter import MULTIPLE, messagebox
from tkinter import filedialog
import os
import textractplus as tp
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
import spacy

# Define path to image
path_to_images = filedialog.askopenfilename(multiple=True)  # saving path of the file location

#Iterate over each file_name in the folder
for file_name in path_to_images:
   
    
    path = r"{}".format(file_name)     # Changing path into String
    
    pdf = re.findall(".pdf", path)           # Checkin for PDF file
     
    docx = re.findall(".docx", path)          # Checking for Docx formated files
    
    doc = re.findall(".doc", path)             # Checking for Doc formated files
    def extract_entities(text):
        for sent in nltk.sent_tokenize(text):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'node'):
                   return chunk.node, ' '.join(c[0] for c in chunk.leaves())
    
    if pdf:
        def extract_text_from_pdf(path):
            return extract_text(path)
        if __name__ == '__main__':
           text = extract_text_from_pdf(path)  # Extracted data from pdf files   
           tokens = nltk.word_tokenize(text)
           tagged = nltk.pos_tag(tokens)
           entities = nltk.chunk.ne_chunk(tagged)
           print(entities) 
          # print(extract_entities(text))