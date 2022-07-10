from typing import Any, Optional, Iterable

from node_and_doublenode import DoubleLinkedNode
from linked_list import LinkedList


class DoubleLinkedList(LinkedList):
    @staticmethod
    def double_linked_nodes(left_node: Optional[DoubleLinkedNode] = None, right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла двусвязного списка.
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node

if __name__ == "__main__":
    dll = LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("________________")
    print("Вывод листа - метод str:")
    print(str(dll))
    print("________________")
    print("Вывод листа - метод repr:")
    print(repr(dll))
    print("________________")
    print("Вывод длины листа:")
    print(dll._len)
    print("________________")
    print("Вставка элемента по индексу:")
    dll.insert(4, 4444)
    print(repr(dll))
    print("________________")
    print("Вставка значения в конец списка:")
    dll.append(4444)
    print(repr(dll))
    print("________________")
    print("вставка элемента по индексу метод setitem")
    dll.__setitem__(2, 2222)
    print(repr(dll))
    print("________________")
    print(f"Вывод элемента по индексу 2 - метод gettitem = {dll.__getitem__(2)}")