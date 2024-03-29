import spacy
nl=spacy.load("en_core_web_sm")
text="Suppose that you went to a hospital for a routine medical check-up. Suppose that the check-up consists of taking your weight and measuring height, checking your blood pressure, taking blood samples, waiting for the doctor’s physical examination,waiting for the result of the blood test, waiting for a chest x-ray, etc."
doc=nl(text)
print('Original' ,text)
print(doc)
print("Noun Phrases:",[chunk.text for chunk in doc.noun_chunks])
print("Verbs:",[token.lemma_ for token in doc if token.pos_=="VERB"])