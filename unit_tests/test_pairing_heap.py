import unittest
from data_structures.pairing_heap import PairingHeap

class TestPairingHeap(unittest.TestCase):

    def test_insert_and_find_min(self):
        ph = PairingHeap()
        ph.insert('A', 10)
        ph.insert('B', 3)
        ph.insert('C', 5)
        node, key = ph.find_min()
        self.assertEqual((node, key), ('B', 3))
        
    def test_duplicate_insert(self):
        ph = PairingHeap()
        ph.insert('A', 5)
        with self.assertRaises(ValueError):
            ph.insert('A', 2)

    def test_extract_min(self):
        ph = PairingHeap()
        ph.insert('A', 10)
        ph.insert('B', 3)
        ph.insert('C', 5)
        node, key = ph.extract_min()
        self.assertEqual((node, key), ('B', 3))
        node, key = ph.extract_min()
        self.assertIn(node, ['A', 'C'])
        self.assertTrue(key in [5, 10])

    def test_decrease_key(self):
        ph = PairingHeap()
        ph.insert('A', 10)
        ph.insert('B', 5)
        ph.decrease_key('A', 1)
        node, key = ph.extract_min()
        self.assertEqual((node, key), ('A', 1))

    def test_decrease_key_missing(self):
        ph = PairingHeap()
        ph.insert('A', 10)
        with self.assertRaises(KeyError):
            ph.decrease_key('Z', 1)

    def test_is_empty_and_len(self):
        ph = PairingHeap()
        self.assertTrue(ph.is_empty())
        ph.insert('X', 8)
        self.assertFalse(ph.is_empty())
        self.assertEqual(len(ph), 1)
        ph.extract_min()
        self.assertTrue(ph.is_empty())

if __name__ == "__main__":
    unittest.main()