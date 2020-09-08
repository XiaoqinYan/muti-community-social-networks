import networkx as nx
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

rnd.seed(19680801)
np.random.seed(19680801)

n=300

G_1 = nx.watts_strogatz_graph(n, 3, 0.05)
G_2 = nx.watts_strogatz_graph(n, 3, 0.05)


G = nx.disjoint_union(G_1, G_2) #merge (G_1 to G_N) as communities of G. 


l=rnd.randint(1,n)

or i in range(l):#add random edges to make the entire society connected
    
    u=rnd.randint(0, n-1)
    v=rnd.randint(n, 2*n-1)
    G.add_edge(u,v)

    communities = sorted(greedy_modularity_communities(G), key=len, reverse=True)

def set_node_community(G, communities):
    '''Add community to node attributes'''
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1
