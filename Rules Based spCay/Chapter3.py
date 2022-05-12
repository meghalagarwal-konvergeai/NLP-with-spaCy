import spacy
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")
doc= nlp("Britain is a place. Mary is a good Docter")

for comp in doc.ents:
    print(comp.text, comp.label_)

from spacy.language import Language

@Language.component("remove_gpe")
def remove_gpe(doc):
    original = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            original.remove(ent)
    doc.ents = original
    return doc

nlp.add_pipe("remove_gpe")

doc= nlp("Britain is a place. Mary is a good Docter")

for comp in doc.ents:
    print(comp.text, comp.label_)