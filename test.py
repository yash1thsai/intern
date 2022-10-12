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
from nltk.tree import Tree
import spacy
from nltk.corpus import treebank
from nameparser.parser import HumanName
nltk.download('treebank')
# Define path to image
path_to_images = filedialog.askopenfilename(multiple=True)  # saving path of the file location

#Iterate over each file_name in the folder
for file_name in path_to_images:
   
    
    path = r"{}".format(file_name)     # Changing path into String
    
    pdf = re.findall(".pdf", path)           # Checkin for PDF file
     
    docx = re.findall(".docx", path)          # Checking for Docx formated files
    
    doc = re.findall(".doc", path)             # Checking for Doc formated files
    '''  def extract_names(txt):
        person_names = []
 
        for sent in nltk.sent_tokenize(txt):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                    person_names.append(
                       ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                    )
        return person_names '''
    
    if pdf:
        def extract_text_from_pdf(path):
            return extract_text(path)
        if __name__ == '__main__':
           text = extract_text_from_pdf(path)  # Extracted data from pdf files
           for sent in nltk.sent_tokenize(text):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
             if hasattr(chunk, 'label'):
               print(chunk.label(), ' '.join(c[0] for c in chunk))