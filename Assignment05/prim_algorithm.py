# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

import networkx as nx
import random

def random_weighted_graph(num_nodes=10, num_edges=20):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    for i in range(num_edges):
        u, v = random.sample(list(G.nodes), 2)
        weight = random.random()
        G.add_edge(u, v, weight=weight)
    return G

def prim_mst(G):
    T = nx.Graph()
    T.add_node(random.choice(list(G.nodes)))
    edge_list = []
    while len(T.nodes) < len(G.nodes):
        for u, v, data in G.edges(T.nodes, data='weight'):
            if v not in T.nodes:
                edge_list.append((u, v, data))
        u, v, weight = min(edge_list, key=lambda x: x[2])
        edge_list.remove((u, v, weight))
        T.add_edge(u, v, weight=weight)
    return T

G = random_weighted_graph()
T = prim_mst(G)
assert nx.is_tree(T)
assert sum(d['weight'] for u, v, d in T.edges(data=True)) == pytest.approx(sum(d['weight'] for u, v, d in G.edges(data=True)))