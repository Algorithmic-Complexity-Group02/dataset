
import networkx as nx
import matplotlib.pyplot as plt

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

G = nx.Graph(graph)

pos= nx.spring_layout(G, k=0.5, iterations=1000)
_, ax = plt.subplots(figsize=(20, 20))

nx.draw_networkx(G, pos, with_labels=False, node_size=10, ax=ax)
ax.axis('off')

plt.show()