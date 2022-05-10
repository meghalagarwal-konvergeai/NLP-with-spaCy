import spacy

nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

import requests
from bs4 import BeautifulSoup
s = requests.get("https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt")
soup = BeautifulSoup(s.content).text.replace("-\n", "").replace("\n", " ")
nlp.max_length = 5278439

doc = nlp(soup)
print (len(list(doc.sents)))

nlp2 = spacy.load("en_core_web_sm")
nlp2.max_length = 5278439

doc = nlp2(soup)
print (len(list(doc.sents)))

nlp.analyze_pipes()

nlp2.analyze_pipes()