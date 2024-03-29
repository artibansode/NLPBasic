import nltk
from nltk.corpus import wordnet
print('synset computer\n')
print(wordnet.synsets("computer"))
print('\nlemma names for computer synset')
print(wordnet.synset("computer.n.01").lemma_names())
print('\n words similar to computer')
#all lemmas for each synset.
for e in wordnet.synsets("computer"):
   print(f'{e} --> {e.lemma_names()}')
# # #print all lemmas for a given synset

print("\nLemmas related to computer \n ")
print(wordnet.synset('computer.n.01').lemmas())
# # #get the synset corresponding to lemma
print(wordnet.lemma('computer.n.01.computing_device').synset())
# # #Get the name of the lemma
print(wordnet.lemma('computer.n.01.computing_device').name())
# # #Hyponyms give abstract concepts of the word that are much more specific
# # #the list of hyponyms words of the computer
print('\n Hyponym : Specific')
syn = wordnet.synset('car.n.01')
print(syn.hyponyms)
print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])
# # #the semantic similarity in WordNet
print('\n Hypernym : General')
vehicle = wordnet.synset('ambulance.n.01')
car = wordnet.synset('car.n.01')
print(car.lowest_common_hypernyms(vehicle))