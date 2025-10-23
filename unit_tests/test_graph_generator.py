import unittest
from utils.graph_generator import generate_graph

class TestGraphGenerator(unittest.TestCase):

    def test_graph_node_count(self):
        g = generate_graph(5, 10)
        self.assertEqual(len(g), 5)

    def test_no_self_loops(self):
        g = generate_graph(5, 20, seed=1)
        for u, neighbors in g.items():
            for v, _ in neighbors:
                self.assertNotEqual(u, v)

    def test_weight_range(self):
        g = generate_graph(5, 20, weight_range=(5, 10), seed=2)
        for _, neighbors in g.items():
            for _, w in neighbors:
                self.assertTrue(5 <= w <= 10)

    def test_reproducibility(self):
        g1 = generate_graph(5, 10, seed=123)
        g2 = generate_graph(5, 10, seed=123)
        self.assertEqual(g1, g2)

if __name__ == "__main__":
    unittest.main()