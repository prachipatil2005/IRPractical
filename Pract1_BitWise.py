import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'this is the first document',
    'this document is second document',
    'and this is a third one',
    'is this first document?',
]

# Create CountVectorizer object
vectorizer = CountVectorizer()

# Fit and transform the corpus into a word count matrix
X = vectorizer.fit_transform(corpus)

# Convert the result to a DataFrame
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Output the DataFrame
print("Generated DataFrame:")
print(df)

# Find indices where both 'this' and 'first' are present
alldata = df[(df['this'] == 1) & (df['first'] == 1)]
print("Indices where both 'this' and 'first' terms are present:", alldata.index.tolist())

# Find indices where either 'this' or 'first' is present
ordata = df[(df['this'] == 1) | (df['first'] == 1)]
print("Indices where either 'this' or 'first' terms are present:", ordata.index.tolist())

# Find indices where 'and' term is present
notdata = df[df['and'] == 1]
print("Indices where 'and' term is present:", notdata.index.tolist())
