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
from tesseract import textractplus as tp
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
import spacy
from nltk import nlp
from spacy.matcher import matcher

from nltk import en_core_web_sm

# Define path to image
path_to_images = filedialog.askopenfilename(multiple=True)  # saving path of the file location

#Iterate over each file_name in the folder
for file_name in path_to_images:
   
    
    path = r"{}".format(file_name)     # Changing path into String
    
    pdf = re.findall(".pdf", path)           # Checkin for PDF file
     
    docx = re.findall(".docx", path)          # Checking for Docx formated files
    
    doc = re.findall(".doc", path)             # Checking for Doc formated files

    def extract_name(resume_text):
        nlp_text = nlp(resume_text)
    
        # First name and Last name are always Proper Nouns
        pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
        
        matcher.add('NAME', None, pattern)
    
        matches = matcher(nlp_text)
    
        for match_id, start, end in matches:
           span = nlp_text[start:end]
        return span.text
    if pdf:
        def extract_text_from_pdf(path):
            return extract_text(path)
        if __name__ == '__main__':
           text = extract_text_from_pdf(path)  # Extracted data from pdf files   
           


           text= extract_name(text)