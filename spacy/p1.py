# Exercise: Reading NLP dataset
# The goal of this exercise is to read the texts and their annotations and then create an IOB format for the tokens in texts.
import spacy
nlp = spacy.load('en_core_web_sm')

print('Abstracts:')
texts = open('./training.abstracts.txt')
for text in texts:
    document = nlp(text)
    print(text)
    for i,s in enumerate(document.sents):
        print(i,s)
        for token in s:
            print('\t',token.orth_, token.pos_)

print()
# print('Annotations:')

# annotations=open('spacy/training.annotations.txt')
# for a in annotations:
#   print(a)