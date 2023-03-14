
import PyPDF2
from nltk.corpus import stopwords
import pandas as pd
from unidecode import unidecode




def process_response(pathPdf):
    
    # Open the PDF file
    pdf_file = open(pathPdf, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract the text from each page
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # Close the PDF file
    pdf_file.close()
    
    #Machine learning model
    

def call_model(text):
   
    stopwords_espanol = stopwords.words('spanish')
    # remove accents from each string in the array
    stopwords_espanol = [unidecode(s) for s in stopwords_espanol]
