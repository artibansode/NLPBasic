import keras
from keras.preprocessing.text import text_to_word_sequence
text="Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."
#text="Hello Everyone..!! Howz u?"
tokens=text_to_word_sequence(text)
print(tokens)