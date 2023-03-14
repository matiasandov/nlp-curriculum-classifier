
import PyPDF2
from nltk.corpus import stopwords
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from unidecode import unidecode
import sklearn
#Documentacion https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
from sklearn.feature_extraction.text import CountVectorizer
import pickle



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
    print(text)
    return call_model(text)
    
    #Machine learning model
    

def call_model(text):
   
    stopwords_espanol = stopwords.words('spanish')
    stopwords_cv = ['correo', 'contacto', 'mail', 'email', 'telefono', 'celular','direccion', 'domicilio', 'perfil']
    stopwords_espanol = stopwords_espanol + stopwords_cv
    stopwords_espanol = [unidecode(s) for s in stopwords_espanol]
    # remove accents from each string in the array

    #strip_accents: Remove accents and perform other character normalization during the preprocessing step.
    vectorizer = CountVectorizer(
        max_features=70,
        lowercase = True, 
        strip_accents = 'ascii',
        analyzer = "word", 
        stop_words = stopwords_espanol)
    0
    data = vectorizer.fit_transform([text])

    

    # Load the saved model weights
    filename = 'naive_model_weights.pkl'
    with open(filename, 'rb') as f:
        saved_clf = pickle.load(f)

    # Instantiate a new MultinomialNB with the saved weights
    new_clf = MultinomialNB()
    new_clf.classes_ = saved_clf.classes_
    new_clf.feature_log_prob_ = saved_clf.feature_log_prob_
    new_clf.class_log_prior_ = saved_clf.class_log_prior_
    prediccion = new_clf.predict(data)
    probabilidad = new_clf.predict_proba(data)
    
    return prediccion, probabilidad


print(process_response("CV DIEGO RUBIO.pdf"))