from nltk.corpus import wordnet
#synonym
print(wordnet.synsets("active"))
#antonyms
print(wordnet.lemma('active.a.01.active').antonyms())