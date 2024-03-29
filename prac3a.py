import nltk
from nltk.corpus import wordnet
print('Synsets realated to the word:Dog')
print(wordnet.synsets("dog"))
# definition and example of the word ‘computer’
print('\n Definition of a particular synset')
print(wordnet.synset("dog.n.01").definition())
# #examples
print('\n examples of its usage')
print("Examples:", wordnet.synset("dog.n.01").examples())
# #get Antonyms
print('\nAntonym os a word')
print(wordnet.lemma('open.v.01.open').antonyms())

