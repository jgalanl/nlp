# Exercise: Reading NLP dataset
# The goal of this exercise is to read the texts and their annotations and then create an IOB format for the tokens in texts.
import spacy
nlp = spacy.load('en_core_web_sm')


class entity:
    def __init__(self, word, type):
        self.word = word
        self.type = type

# Encontrar los nombres de los medicamentos en las anotaciones

print('Annotations:')

annotations=open('spacy/training.annotations.txt')
annotations_list = []

for annotation in annotations:
    annotations_splited = annotation.split('\t')
    annotations_words = annotations_splited[4].split(' ')
    for annotation_word in annotations_words:
        if annotation_word not in annotations_list:
            annotations_list.append(annotation_word)

# print('Abstracts:')
# texts = open('./training.abstracts.txt')
# for text in texts:
#     document = nlp(text)
#     print(text)
#     for i,s in enumerate(document.sents):
#         print(i,s)
#         for token in s:
#             print('\t',token.orth_, token.pos_)