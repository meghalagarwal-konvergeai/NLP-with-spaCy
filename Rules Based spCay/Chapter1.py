#Import the requisite library
import spacy

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")
#Sample text
text = "The village of Treblinka is in Poland. Treblinka was also an extermination camp."
#Create the Doc object
doc = nlp(text)
#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)

#Import the requisite library
import spacy

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")
#Sample text
text = "The village of Treblinka is in Poland. Treblinka was also an extermination camp."
#Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler")
#List of Entities and Patterns
patterns = [{"label": "GPE", "pattern": "Treblinka"}]

ruler.add_patterns(patterns)

doc = nlp(text)
#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)

nlp.analyze_pipes()

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")
#Sample text
text = "The village of Treblinka is in Poland. Treblinka was also an extermination camp."
#Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler", after="ner")

#List of Entities and Patterns
patterns = [{"label": "GPE", "pattern": "Treblinka"}]

ruler.add_patterns(patterns)

doc = nlp(text)
#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)

#Import the requisite library
import spacy

#Sample text
text = "This is a sample number (555) 555-5555."
#Build upon the spaCy Small Model
nlp = spacy.blank("en")
#Create the Ruler and Add it
ruler = nlp.add_pipe("entity_ruler")

#List of Entities and Patterns (source: https://spacy.io/usage/rule-based-matching)
patterns = [
                {"label": "PHONE_NUMBER", "pattern": [{"ORTH": "("}, {"SHAPE": "ddd"}, {"ORTH": ")"}, {"SHAPE": "ddd"},
                {"ORTH": "-", "OP": "?"}, {"SHAPE": "dddd"}]}
            ]
#add patterns to ruler
ruler.add_patterns(patterns)

#create the doc
doc = nlp(text)
#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)