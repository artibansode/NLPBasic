import nltk
from nltk.stem import RegexpStemmer
word_stemmer=RegexpStemmer('ing$|s$|e$|able$|al$',min=4)
print(word_stemmer.stem('writing'))
print(word_stemmer.stem('cars'))
print(word_stemmer.stem('write'))
print(word_stemmer.stem('advisable'))
print(word_stemmer.stem('statistical'))