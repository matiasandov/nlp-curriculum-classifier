# nlp-curriculum-classifier

NLP repository with projects like Article Classifiers, Recommender Systems and Text Processing

Selection of CVs with Machine Learning

A Natural Language Processing model using Machine Learning was developed, in which Python libraries such as NLTK, Sklearn and TensorFlow were used to process the text input of CVs using techniques such as:

Elimination of Spanish "stop words" and specific ones for CVs
Processing CV words as Count Vectors and limiting them to the 70 most significant words
Removing accents
Once the text was vectorized, it went through two classifiers: an Artificial Neural Network (ANN) and a discriminatory classifier called Naive Bayes. The latter was trained with input data to later predict whether a CV would be classified as "considered" or "not considered" based on historical data, obtaining a probability of belonging to its respective class. After training and testing both models, it was decided to use the classifier trained with an ANN because it showed an accuracy score of 77% for test data, while Naive Bayes varied between 50% and 70%.

Additionally, a model was developed to find similarity between a job position and a CV using cosine similarity. With this model, a Terra recruiter can determine if a CV is appropriate for follow-up with the press of a button, which takes only a few minutes compared to the traditional approach.

Finally, everything was integrated into a simple Python application developed with PySimpleGUI where a CV can be selected and a prediction can be made for it.

The selected final ANN model can be observed in the `nlp-curriculum-classifier/curriculumClassifierTerra/ANN_classifier_oficial.ipynb` ANN_classifier_oficial.ipynb file, while the final trained Naive Bayes model is in the naive_bayes_oficial.ipynb file. The vector similarity model, which was not deployed in the app, is in jobMatching.ipynb. The PySimpleGUI interface is also included.

_______________________________________________________________________

- Selección de CV’s con Machine Learning
Lo que se realizó fue un modelo de Natural Language Processing de Machine Learning, en el que usando librerías como NLTK, Sklearn y TensorFlow de Python, pudimos procesar las entradas del texto de los CV’s ocupando técnicas como:
Eliminación de “stop words” en español y específicas para los CV’s
Tratar las palabras en los CV’s como Count Vectors y limitarlas a las 70 palabras más significativas del CV.
Remover acentos.

	Una vez que el texto se vectoriza, este pasó por dos clasificadores, uno cpnstruido con una Red Neuronal Artificial y otro discriminatorio llamado Naive Bayes, el cuál se encargó de entrenarse con ciertos datos de entrada para poder después hacer predicciones de si un CV se clasificará como “considerado” o “no considerado” al haber aprendido de los datos históricos y obteniendo una probabilidad de pertenecer a su respectiva clase. Tras haber entrenado y probar ambos modelos decidimos usar el clasificador entrenado con una ANN ya que este mostró un score de accuracy de 77% para los datos de prueba, mientras que Naive Bayes variaba entre 50% y 70%. 


 Asimismo se desarrolló un modelo para encontrar similaridad entre una posición de trabajo y un CV, usando similaridad cosénica. Se dice que a un reclutador de Terra le toma unos minutos para darse cuenta si un CV es apropiado o no para darle seguimiento, con este modelo es cuestión de picar un botón.

Asimismo, se unió todo en una sencilla aplicación de Python desarrollada con PySimpleGUI donde se selecciona un CV y se hace una predicción para este.

- El modelo final de la ANN seleccionado puede ser observado en el archivo ANN_classifier_oficial.ipynb
- El modelo final entrenado de Naive bayes puede ser observado en el archivo naive_bayes_oficial.ipynb
- El modelo de similaridad vectorial que al final no se hizo deploy en la app está en jobMatching.ipynb
La interface de PySimpleGUi 
