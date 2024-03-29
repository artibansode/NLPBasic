import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print("word:\t lemma")
print("rocks:",lemmatizer.lemmatize("rocks"))
print("corpora:",lemmatizer.lemmatize("corpora"))
print("mice:",lemmatizer.lemmatize("mice"))
print("pharmacies:",lemmatizer.lemmatize("pharmacies"))
print("following:",lemmatizer.lemmatize("following",pos='n'))
print("following:",lemmatizer.lemmatize("following",pos='v'))
print("better:",lemmatizer.lemmatize("better",pos="a"))