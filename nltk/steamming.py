import nltk
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()

sentence='The boys have listened to lots of sad stories.'
tokens=nltk.word_tokenize(sentence)

for t in tokens:
    print(t,'\t\t',porter.stem(t))