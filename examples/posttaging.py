import nltk

# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

text="Esta es la asignatura TESI. Este es un curso de NLP. El segundo tema está dedicado a NLTK, Spacy y expresiones regulares."
tokens = nltk.word_tokenize(text)
tags=nltk.pos_tag(tokens)
# print(tags)
print(nltk.ne_chunk(tags))