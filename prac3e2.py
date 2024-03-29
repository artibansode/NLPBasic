import gensim
import nltk
from nltk import word_tokenize
from gensim.parsing.preprocessing import remove_stopwords

text="Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."
print("Original Text :\n "+text)

filtered_sentence=remove_stopwords(text)
print("Removing stopwords :\n ")
print(filtered_sentence)

all_stopwords=gensim.parsing.preprocessing.STOPWORDS
#print(all_stopwords)

 # Adding new stopwords
from gensim.parsing.preprocessing import STOPWORDS
all_stopwords_gensim=STOPWORDS.union(set(['blood','check-up']))
text_tokens=word_tokenize(text)

final=[word for  word in text_tokens if word not in all_stopwords_gensim]
print("Adding custom stopwords blood and check-up:\n ")
print(final)