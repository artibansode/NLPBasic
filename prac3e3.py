import nltk
from nltk import word_tokenize

import spacy
sp=spacy.load('en_core_web_sm')

text="Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."
print("\n Original Text",text)
text_tokens=word_tokenize(text)
print("\n Original Tokens",text_tokens)


all_Stopwords=sp.Defaults.stop_words
all_Stopwords.add('Suppose')


tokens_without_sw=[word for word in text_tokens if not word in all_Stopwords]
print("\n Tokens withput Stopwords",tokens_without_sw)

print('\n Removing a stopword from list \n')
all_Stopwords.remove('Suppose')
tokens_without_sw=[word for word in text_tokens if not word in all_Stopwords]
print(tokens_without_sw)