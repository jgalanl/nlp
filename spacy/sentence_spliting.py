# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')

text = open("./text_spacy.txt").read()
document = nlp(text)

for i,s in enumerate(document.sents):
    print(i,s)
    for token in s:
     print('\t',token.orth_, token.pos_)

 