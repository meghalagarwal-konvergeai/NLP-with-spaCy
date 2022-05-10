import spacy

nlp = spacy.load("en_core_web_sm")

with open("/home/meghal/Personal/Konverge_AI/Training/NLP with SaCy/Data/wiki_us.txt","r") as f:
    text = f.read()

doc = nlp(text)

# Difference between iterating through text and itterating through doc
print(len(text))
print(len(doc))

'''
Sentence Boundary Detection (SBD)
--->In NLP, sentence boundary detection, or SBD, is the identification of sentences in a text.
'''
for sentence in doc.sents:
    print(sentence,"\n")