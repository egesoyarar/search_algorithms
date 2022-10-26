import unittest
from breadthFirstSearch import bfs

class SearchAlgorithms(unittest.TestCase):

    def test_bfs_solvable(self):
        root = "A"
        nodes = {"A":["B","C"], "B":["A","D","E"], "C":["F","G"], "D":["A"], "E":["K"]}
        dest = "K"

        result = bfs(root, nodes, dest)
        self.assertTrue(result)

    def test_bfs_unsolvable(self):
        root = "A"
        nodes = {"A":["B","C"], "B":["A","D","E"], "C":["F","G"], "D":["A"], "E":["K"]}
        dest = "H"

        result = bfs(root, nodes, dest)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()