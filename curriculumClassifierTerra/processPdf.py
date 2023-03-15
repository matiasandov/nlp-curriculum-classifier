
import PyPDF2
from nltk.corpus import stopwords
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from unidecode import unidecode
import sklearn
#Documentacion https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
from sklearn.feature_extraction.text import CountVectorizer
import pickle
#Procesaamiento del input
import re 
import nltk 

# Stopwords
nltk.download("stopwords") 
from nltk.corpus import stopwords 

# Stemming --> get root of the word
from nltk.stem.porter import PorterStemmer 
from nltk.stem import SnowballStemmer # best stemmer


# Lemmatization --> get context
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem.wordnet import WordNetLemmatizer



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
    
    return call_model(text)
    
    #Machine learning model
    

def call_model(text):
   
    
    #Porcesamiento input
    eliminarAcentos = lambda str: str.translate(str.maketrans("áàäéèëíìïòóöùúüÀÁÄÈÉËÌÍÏÒÓÖÙÚÜ", "aaaeeeiiiooouuuAAAEEEIIIOOOUUU"))

   

    # 0. Quitamos acentos:
    review = eliminarAcentos(text[0])
    # 1. Quitamos todo lo que no sea una letra:
    review = re.sub("[^a-zA-Z]", " ", review) 
    # 2. Todo en minúsculas:
    review = review.lower()
    # 2.1 Quitamos espacios multiples y dejamos solo uno:
    review = re.sub("[\s]+", " ", review)

    # 2.2 Extra: Quitar palabras de menos de 3 letras y espacios al principio y final
    review = re.sub(r"\W*\b\w{1,3}\b", "", review)
    review = review.strip()

    # 3. Separamos oraciones para obtener puras palabras
    review = review.split()

    # 4. Extraer el significado detrás de cada palabra Stemming o Lemmatization y eliminar ruido
    #stemmer = SnowballStemmer('spanish') # Best stemmer
    #ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # 4.1 Además queremos quitar palabras irrelevantes como artículos
    all_stopwords = stopwords.words("spanish") 
    #all_stopwords.remove("palabra") # --> para excepciones que no queramos incluir

    # 4.2 Unimos el Stemmer/Lematization para cada palabra que no esté dentro de la lista de stopwords
    #review = [stemmer.stem(word) for word in review if word not in set(all_stopwords)]
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(all_stopwords)]
    #review = [word for word in review if word not in set(all_stopwords)]
    review = [" ".join(review)]
    
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(review).toarray()


    

    pickled_model = pickle.load(open('ann_model_weights.pkl', 'rb'))
    prediccion = pickled_model.predict(X)
  
    #Probabilidad numerica
    #probabilidad = new_clf.score(data, prediccion)
    #prediccion = prediccion[0]
    #probabilidad = max(probabilidad)
    
    print(prediccion)
    return prediccion


print(process_response("Bestie.pdf"))