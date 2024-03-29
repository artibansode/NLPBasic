import nltk
from nltk import tokenize
from nltk import tag
from nltk import chunk
para="Hi!Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."
print('Original Text',para)
sents=tokenize.sent_tokenize(para)
print("Sentence Segmentation:\n",sents)

print("\n Word Tokenization")
for index in range(len(sents)):
    words=tokenize.word_tokenize(sents[index])
    print(words)
    
tagged_words=[]
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
print("\n POS Tagging\n",tagged_words)
 
 
tree=[]
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
print("\n chunking \n")
print(tree)