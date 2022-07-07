from typing import Any, Optional

from Node import Node

class DoubleLinkedNode(Node):
    """Дочерний класс который описывает двусвязный список"""
    def __init__(self, value = None, next_ = None, prev_ = None):
        """
        Инициализация атрибутов класса с помощью наследования super()
        :param value: Любое значение, которое помещено в узел
        :param next_: Следующий узел, если он есть
        :param prev_: Предыдущий элемент, если он есть
        """
        super().__init__(value, next_)
        self.prev = prev_

    @property
    def prev(self):
        """
        Декоратор (getter) - метод, получения доступа к атрибуту
        :return:
        """
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"] = None):
        """
        Декоратор (Setter) - метод, изменения/установления значения атрибутов
        :param prev_:
        :return:
        """
        self.is_valid(prev_)
        self._prev = prev_



if __name__ == '__main__':
    node_1 = DoubleLinkedNode(1)
    node_2 = DoubleLinkedNode(2)
    node_3 = DoubleLinkedNode(3)

    node_1.next = node_2
    node_2.next = node_3

    node_2.prev = node_1
    node_3.prev = node_2

    print(repr(node_1))
    print(repr(node_2))
    print(repr(node_3))