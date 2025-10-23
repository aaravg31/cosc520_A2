"""
Simple random weighted graph generator for benchmarking Dijkstra’s algorithm.
Generates a directed graph represented as an adjacency list (dictionary).
"""

import random

def generate_graph(num_nodes, num_edges, weight_range=(1, 10), seed=None):
    """
    Generate a random directed graph.

    Parameters
    ----------
    num_nodes : int
        Number of nodes (vertices)
    num_edges : int
        Number of edges
    weight_range : tuple(int, int), optional
        Minimum and maximum weight for edges
    seed : int, optional
        Random seed for reproducibility

    Returns
    -------
    dict
        Graph represented as {node: [(neighbor, weight), ...]}
    """
    if seed is not None:
        random.seed(seed)

    # Initialize adjacency list
    graph = {i: [] for i in range(num_nodes)}

    # Randomly connect nodes
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u == v:
            continue  # skip self-loops
        w = random.randint(weight_range[0], weight_range[1])
        graph[u].append((v, w))

    return graph