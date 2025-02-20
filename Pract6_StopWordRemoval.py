import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Corrected sentence (typos fixed)
example_sent = "The athletes from the school competed in the regional tournament"

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Tokenize the sentence
word_tokens = word_tokenize(example_sent)

# Remove the redundant list comprehension (keep only the for loop)
filtered_sentence = []
for w in word_tokens:
    if w.lower() not in stop_words:  # Added .lower() to handle case sensitivity
        filtered_sentence.append(w)

# Print results
print("Word Tokens:", word_tokens)
print("Filtered Sentence:", filtered_sentence)
