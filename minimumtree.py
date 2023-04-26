from ctypes import pythonapi
from gettext import install
import pip
import networkx as nx
import matplotlib as plt
from networkx.algorithms import tree

G = nx.cycle_graph(4)
G.add_edge(0, 3, weight=2)
mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
edgelist = list(mst)
sorted(sorted(e) for e in edgelist)
[[0, 1], [1, 2], [2, 3]]