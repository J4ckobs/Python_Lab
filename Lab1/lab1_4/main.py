from typing import Any
from collections import deque
import unittest


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.children = {}

class Tree:
    def __init__(self, root_value: Any):
        self.root = Node(root_value)

    def add_child(self, parent, child_value, edge_value=None):
        child = Node(child_value)
        parent.children[child] = edge_value
        return child

    def bfs_traverse(self):
        result, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node)
            queue.extend(node.children.keys())
        return result


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree("A")

    def test_tree_creation(self):
        b = self.tree.add_child(self.tree.root, "B", 1)
        c = self.tree.add_child(self.tree.root, "C", 2)

        self.assertEqual(len(self.tree.root.children), 2)
        self.assertEqual(self.tree.root.children[b], 1)
        self.assertEqual(self.tree.root.children[c], 2)

    def test_bfs_traverse(self):
        b = self.tree.add_child(self.tree.root, "B")
        c = self.tree.add_child(self.tree.root, "C")
        self.tree.add_child(b, "D")

        nodes = [node.value for node in self.tree.bfs_traverse()]
        self.assertEqual(nodes, ["A", "B", "C", "D"])


if __name__ == '__main__':
    unittest.main()