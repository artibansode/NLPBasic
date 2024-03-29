import nltk
from nltk.stem import LancasterStemmer
word_stemmer=LancasterStemmer()
print(word_stemmer.stem('writing'))
print(word_stemmer.stem('living'))