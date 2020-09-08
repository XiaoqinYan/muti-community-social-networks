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
            
            def set_edge_community(G):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0

            def get_color(i, r_off=1, g_off=1, b_off=1):
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)

set_node_community(G, communities)
set_edge_community(G)

# Set community color for nodes
node_color = [get_color(G.nodes[v]['community']) for v in G.nodes]

# Set community color for internal edges
external = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] == 0]
internal = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] > 0]
internal_color = [get_color(G.edges[e]['community']) for e in internal]

pos = nx.spring_layout(G, k=0.2)
#nx.draw_networkx(
#  G, pos=pos, node_size=0, edge_color="#333333", alpha=0.5, with_labels=False)

nx.draw_networkx(
   G, pos=pos, node_size=0, edgelist=external, edge_color="#333333",
   alpha=0.6, with_labels=False)
# Draw internal edges
nx.draw_networkx(
   G, pos=pos, node_size=0, edgelist=internal, edge_color=internal_color,
   alpha=0.4, with_labels=False)
