import nltk

from nltk.tokenize import RegexpTokenizer

tk=RegexpTokenizer('\s+',gaps=True)
str="Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."

tokens=tk.tokenize(str)
print(tokens)