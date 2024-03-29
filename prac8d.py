nimport nltk
from nltk.stem import SnowballStemmer
word_stemmer=SnowballStemmer('english')
print(word_stemmer.stem('writing'))