from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
documents=["i love the test of indian food","i love the test of italian food","i love the test of chinese food","i love the test of mexican food","i love the test of thai food","i love the test of japanese food","i love the test of korean food","i love the test of american food","i love the test of french food","i love the test of spanish food"]
vectorizer=TfidfVectorizer(stop_words='english')
tfidf_matrix=vectorizer.fit_transform(documents)
num_clusters=3
KMeans=KMeans(n_clusters=num_clusters,random_state=42)
KMeans.fit(tfidf_matrix)
labels=KMeans.labels_
for i,doc in enumerate(documents):
    print(f"Document {i+1} :{doc}")
    print(f"Cluster:{labels[i]}\n")
silhouette_avg=silhouette_score(tfidf_matrix,labels)
print(f"Silhouette Score:{silhouette_avg:.3f}")

# The Silhouette Score is a metric used to measure the quality of clustering. It calculates how similar an object is to its own cluster compared to other clusters. The score ranges from -1 to +1:

# +1 indicates that the sample is well clustered.
# 0 indicates that the sample is on or very close to the decision boundary between two clusters.
# -1 indicates that the sample is poorly clustered.
# A higher Silhouette Score means better-defined clusters. It's commonly used to evaluate clustering algorithms like K-means.
# TF measures how frequently a word appears in a document.
# IDF reduces the weight of common words across all documents.