import sklearn
#Documentacion https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
from sklearn.feature_extraction.text import CountVectorizer
#strip_accents: Remove accents and perform other character normalization during the preprocessing step.
vectorizer = CountVectorizer(lowercase = True, strip_accents = True, analyzer = "word", stop_words = "english")
vectorizer.fit(list_of_documents_train)
Xtrain = vectorizer.transform(list_of_documents_train)
# all in one step
#Esto te da la matrix of counts y fits the model at the same time
Xtrain = vectorizer.fit_transform(list_of_documents_train)
Xtest = vectorizer.transform (list_of_documents_test)