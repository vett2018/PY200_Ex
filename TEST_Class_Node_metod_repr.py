import unittest

from Node import Node

class TestCase(unittest.TestCase):
    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node("node_without_next")

        msg = "Значение представления __repr__ некорректно для узла без следующего узла. "
        self.assertEqual(repr(node), "Node(node_without_next, None)", msg)
