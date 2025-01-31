from nltk import word_tokenize
from nltk.util import ngrams

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text.lower())

# Unigram
unigram = list(ngrams(tokens, 1))
print(f"Unigram: {unigram}")

# Bigrams
bigrams = list(ngrams(tokens, 2))
print(f"Bigrams: {bigrams}")

# Trigrams
trigrams = list(ngrams(tokens, 3))
print(f"Trigrams: {trigrams}")

print('Tokens:', tokens)
