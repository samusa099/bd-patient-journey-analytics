from collections import defaultdict
import heapq
def build_graph(edges):
 g=defaultdict(list)
 for e in edges:g[e["from_node"]].append((e["to_node"],float(e["expected_walk_min"])))
 return g
