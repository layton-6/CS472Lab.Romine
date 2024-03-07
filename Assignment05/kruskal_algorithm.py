# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

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

def kruskal_mst(G):
    T = nx.Graph()
    edge_list = sorted((u, v, data) for u, v, data in G.edges(data='weight'))
    components = {node: node for node in G.nodes}
    for u, v, weight in edge_list:
        if components[u] != components[v]:
            T.add_edge(u, v, weight=weight)
            new_component = {components[u], components[v]}
            for node in G.nodes:
                if components[node] == components[u]:
                    components[node] = new_component
                elif components[node] == components[v]:
                    components[node] = new_component
    return T

G = random_weighted_graph()
T = kruskal_mst(G)
assert nx.is_tree(T)
assert sum(d['weight'] for u, v, d in T.edges(data=True)) == pytest.approx(sum(d['weight'] for u, v, d in G.edges(data=True)))