from nltk.tokenize import MWETokenizer
from nltk import sent_tokenize,word_tokenize
s="Good cake costs 1500/kg in a New York bakery near telephone booth in hong kong ."
MWE=MWETokenizer([('New','York'),('telephone','booth'),('hong','kong')],separator='-')
for sent in sent_tokenize(s):
	print(MWE.tokenize(word_tokenize(sent)))