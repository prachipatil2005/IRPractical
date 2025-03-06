import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()
G.add_edges_from([(1,2),(1,3),(2,3),(3,1)])
pagerank_scores=nx.pagerank(G)
hits_scores=nx.hits(G)
print("PageRank Scores: ",pagerank_scores)
print("Hits Scores: ",hits_scores[0])
print("Authority Scores: ",hits_scores[1])
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,node_color='blue',edge_color='red',node_size=2000,font_size=15,font_weight='bold')
plt.title('Directed graph with PageRank Scores')
plt.show()