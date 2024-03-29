import nltk
from nltk.corpus import stopwords
#nltk.download('stopwords')

from nltk.tokenize import word_tokenize

text="Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."
print('Original Text :\n'+text)
text_tokens=word_tokenize(text)
print('Tokenization :\n')
print(text_tokens)

print('\n Tokens without stopwords (nltk) :\n')
tokens_without_sw=[word for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw)

print('\n Adding a custom stopword to the list \n')
all_Stopwords=stopwords.words('english')
all_Stopwords.append('blood')
all_Stopwords.append('Suppose')
tokens_without_sw=[word for word in text_tokens if not word in all_Stopwords]
print(tokens_without_sw)

print('\n Removing a stopword from list \n')
all_Stopwords.remove('blood')
tokens_without_sw=[word for word in text_tokens if not word in all_Stopwords]
print(tokens_without_sw)