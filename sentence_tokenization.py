import nltk


# Prueba nltk con un texto en ingles
text = "Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice."
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
    print(sentence)
    print()

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    print(words)
    print()


# Prueba nltk con un texto en español
# tokenizer_es = nltk.data.load('tokenizers/punkt/spanish.pickle')
# text='Esta es la asignatura TESI. Este es un curso de NLP. El segundo tema está dedicado a NLTK, Spacy y expresiones regulares.'
# sentences=tokenizer_es.tokenize(text)
# for s in sentences:
#   print(s)