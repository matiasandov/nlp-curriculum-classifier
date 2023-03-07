import nltk 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download ("wordnet") # only need to do once
lemmatizer = WordNetLemmatizer ()
lemmatizer.lemmatize("mice") # returns 'mouse'

#Note: "pos" stands for "parts-of-speech"
lemmatizer.lemmatize ("going") # returns 'going'
lemmatizer.lemmatize ("going", pos = wordnet.VERB) # returns 'go'