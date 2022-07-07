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

if __name__ == '__main__':
