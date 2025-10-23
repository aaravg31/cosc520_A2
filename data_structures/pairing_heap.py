"""
Pairing Min Heap

Implements:
- insert(node, priority)
- extract_min() -> (node, priority) or (None, None) if empty
- find_min() -> (node, priority) or (None, None) if empty
- is_empty() -> bool
- __len__() -> number of items

Notes
-----
- A simplified heap of heap-ordered trees linked through sibling pointers.
- Performs very well in practice, similar to Fibonacci heaps.
- Amortized complexities:
  * Insert: O(1)
  * Extract-Min: O(log n)
  * Decrease-Key: O(log n) (optional, not implemented here)
"""

from typing import Any, Optional


class PairNode:
    def __init__(self, node: Any, key: float):
        self.node = node
        self.key = key
        self.left_child: Optional["PairNode"] = None
        self.next_sibling: Optional["PairNode"] = None
        self.prev: Optional["PairNode"] = None


class PairingHeap:
    def __init__(self):
        self.root: Optional[PairNode] = None
        self.count = 0
        self.nodes = {}

    # INSERT
    def insert(self, node: Any, priority: float) -> None:
        if node in self.nodes:
            raise ValueError(f"Node {node!r} already present in heap.")
        new_node = PairNode(node, priority)
        self.nodes[node] = new_node
        self.root = new_node if self.root is None else self._compare_and_link(self.root, new_node)
        self.count += 1

    # FIND MIN
    def find_min(self):
        if self.root is None:
            return None, None
        return self.root.node, self.root.key

    # EXTRACT MIN
    def extract_min(self):
        if self.root is None:
            return None, None
        min_node = self.root
        result = (min_node.node, min_node.key)
        del self.nodes[min_node.node]

        if self.root.left_child is None:
            self.root = None
        else:
            self.root = self._combine_siblings(self.root.left_child)

        self.count -= 1
        return result

    # IS EMPTY
    def is_empty(self) -> bool:
        return self.root is None

    # LEN
    def __len__(self) -> int:
        return self.count

    # INTERNAL UTILITIES
    def _compare_and_link(self, first: PairNode, second: Optional[PairNode]) -> PairNode:
        if second is None:
            return first
        if second.key < first.key:
            second.prev = None
            first.prev = second
            first.next_sibling = second.left_child
            if first.next_sibling:
                first.next_sibling.prev = first
            second.left_child = first
            return second
        else:
            second.prev = first
            second.next_sibling = first.left_child
            if second.next_sibling:
                second.next_sibling.prev = second
            first.left_child = second
            return first

    def _combine_siblings(self, first_sibling: PairNode) -> PairNode:
        if first_sibling.next_sibling is None:
            return first_sibling

        tree_array = []
        while first_sibling:
            tree_array.append(first_sibling)
            next_sib = first_sibling.next_sibling
            first_sibling.next_sibling = None
            first_sibling = next_sib

        i = 0
        while i + 1 < len(tree_array):
            tree_array[i] = self._compare_and_link(tree_array[i], tree_array[i + 1])
            i += 2

        j = i - 2
        if j == len(tree_array) - 3:
            tree_array[j] = self._compare_and_link(tree_array[j], tree_array[j + 2])
        while j >= 2:
            tree_array[j - 2] = self._compare_and_link(tree_array[j - 2], tree_array[j])
            j -= 2

        return tree_array[0]
