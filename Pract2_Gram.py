# NLTK (Natural Language Toolkit) 
import nltk
nltk.download('punkt_tab')


import nltk
from nltk import word_tokenize
from nltk.util import ngrams
text="This is a text for unigrams,bigrams,and trigrams extraction using NLTK"
tokens=word_tokenize(text.lower())
unigrams=list(ngrams(tokens,1))
bigrams=list(ngrams(tokens,2))
trigram=list(ngrams(tokens,3))
print("Original Text:",text)
print("\nUnigrams:",unigrams)
print("\Bigrams:",bigrams)
print("\Trigram:",trigram)

