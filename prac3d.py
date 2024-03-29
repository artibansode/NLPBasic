import nltk
from nltk.corpus import wordnet

syn1=wordnet.synsets('football')
syn2=wordnet.synsets('soccer')

#print(syn1.path_similarity(syn2))

for s1 in syn1:
    for s2 in syn2:
        print('Path similarity of:')
        print(s1,'(',s1.pos(),')','[',s1.definition(),']')
        print(s2,'(',s2.pos(),')','[',s2.definition(),']')
print(" Similarity is",s1.path_similarity(s2))
        