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
# for sentence in doc.sents:
#     print(sentence,"\n")

# "doc.sents" is a generator function, hence to use a genetor function it is required to convert into list
sent1 = list(doc.sents)[0]
print(sent1)

'''
Token Attributes:
-->The token object contains a lot of different attributes that are VITAL do performing NLP in spaCy. We will be working with a few of them, such as:
.text
.head
.left_edge
.right_edge
.ent_type_
.iob_
.lemma_
.morph
.pos_
.dep_
.lang_
'''
tok = sent1[2]
print(tok.text)
print(tok.head)
print(tok.left_edge)
print(tok.right_edge)
print(tok.ent_type_)
print(tok.ent_iob_)
print(tok.lemma_)
print(tok.morph)
print(tok.pos_)
print(tok.dep_)
print(tok.lang_)

'''
Part of Speech Tagging (POS)
-->In the field of computational linguistics, understanding parts-of-speech is essential.
SpaCy offers an easy way to parse a text and identify its parts of speech.
Below, we will iterate across each token (word or punctuation) in the text and identify its part of speech.
'''

statment = "My name is Meghal Agarwal"
doc2 = nlp(statment)
for tok in doc2:
    print(tok.text, tok.pos_, tok.dep_)

from spacy import displacy
#print(displacy.render(doc2, style="dep"))


print(displacy.render(doc,style="ent"))