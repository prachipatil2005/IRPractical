import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def cosine_similarity(x,y):
    if len(x)!=len(y):
        return None
    dot_product=np.dot(x,y) 
    magnitude_x=np.sqrt(np.sum(x**2))
    magnitude_y=np.sqrt(np.sum(y**2))
    cosine_similariry=dot_product/(magnitude_x*magnitude_y)
    return cosine_similariry
corpus=['I am going to the store because i lost my keys','the manager and his team worked very hard to complete the project on time','Ankur was happy becase he hot a gift']
X=CountVectorizer().fit_transform(corpus).toarray()
print(X)
cos_sim_1_2=cosine_similarity(X[0,:],X[1,:])
cos_sim_1_3=cosine_similarity(X[0,:],X[2,:])
cos_sim_2_3=cosine_similarity(X[1,:],X[2,:])
print('Cosine similarity between:')
print('\tDocumnet 1 and Document 2:',cos_sim_1_2)
print('\tDocumnet 1 and Document 3:',cos_sim_1_3)
print('\tDocumnet 2 and Document 3:',cos_sim_2_3)

# Ranges between -1 and 1.
# 1: Vectors are identical.
# 0: Vectors are orthogonal (no similarity).
# -1: Vectors are opposite.
# Explain that this technique is widely used in search engines, recommendation systems, and text clustering to find related documents or items based on textual similarity.