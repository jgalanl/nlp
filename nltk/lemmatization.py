import nltk
# python3 -m nltk.downloader wordnet
# python3 -m nltk.downloader punkt
from nltk.stem import WordNetLemmatizer

sentence='The boys have listened to lots of sad stories.'
tokens=nltk.word_tokenize(sentence)
lematizer = WordNetLemmatizer()
print('Token:\t\tLemma:')
for t in tokens:
    print(t,'\t\t',lematizer.lemmatize(t))

