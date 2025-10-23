"""
Dijkstra's Shortest Path Algorithm

Implements:
- dijkstra(graph, source, heap_type="binary")

Parameters
----------
graph : dict
    Adjacency list {u: [(v, weight), ...]}.
source : Any
    Starting node.
heap_type : str
    One of {"binary", "pairing", "fibonacci"}.

Returns
-------
dict
    Mapping of node -> shortest distance from source.
"""

import math
from data_structures.binary_heap import BinaryHeap
from data_structures.fibonacci_heap import FibonacciHeap
from data_structures.pairing_heap import PairingHeap


def dijkstra(graph, source, heap_type="binary"):
    # Initialize heap based on type
    if heap_type == "binary":
        heap = BinaryHeap()
    elif heap_type == "fibonacci":
        heap = FibonacciHeap()
    elif heap_type == "pairing":
        heap = PairingHeap()
    else:
        raise ValueError("heap_type must be one of {'binary', 'pairing', 'fibonacci'}")

    # Initialize distances
    dist = {v: math.inf for v in graph}
    dist[source] = 0

    # Insert source
    heap.insert(source, 0)

    while not heap.is_empty():
        u, d = heap.extract_min()
        if u is None:
            continue
        if d > dist[u]:
            continue  # Skip outdated entries

        for v, w in graph.get(u, []):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt

                # Check if node already exists in heap for decrease-key
                if (hasattr(heap, "nodes") and v in heap.nodes) or (hasattr(heap, "_pos") and v in heap._pos):
                    heap.decrease_key(v, alt)
                else:
                    heap.insert(v, alt)

    return dist
