# Many languages are included, such as English, German, Spanish, and Arabic.
# Check:
# ~/nltk_data/corpora/stopwords/
# But note that not all languages are supported.

#Para usar NLKT tengo que usar el envirment de Python 3.11 64 bit
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words ('english')
stopwords.words ('german')