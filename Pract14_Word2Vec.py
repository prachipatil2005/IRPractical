import nltk
import gensim
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")

documents = [
    "Information retrieval is a key area in search engines.",
    "Machine learning helps improve search relevance.",
    "Deep learning and AI are advancing information retrieval.",
    "Search engines use algorithms to rank results.",
    "Artificial intelligence enhances text processing."
]

# Tokenize documents
tokenized_docs = [word_tokenize(doc.lower()) for doc in documents]

# Train Word2Vec model
word2vec_model = gensim.models.Word2Vec(tokenized_docs, vector_size=100, window=5, min_count=1, workers=4)

# Function to get sentence vector
def get_sentence_vector(sentence, model):
    words = word_tokenize(sentence.lower())
    vectors = [model.wv[word] for word in words if word in model.wv]

    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

# Function to perform search
def search(query):
    query_vector = get_sentence_vector(query, word2vec_model)
    doc_vectors = np.array([get_sentence_vector(doc, word2vec_model) for doc in documents])

    scores = cosine_similarity([query_vector], doc_vectors)[0]
    ranked_results = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

    print("\nSearch Results for:", query)
    found_results = False

    for i, score in ranked_results:
        if score > 0:
            print(f"Score: {score:.4f} | Document: {documents[i]}")
            found_results = True

    if not found_results:
        print("No relevant results found.")

# Get user query and perform search
query = input("Enter search query: ")
search(query)
