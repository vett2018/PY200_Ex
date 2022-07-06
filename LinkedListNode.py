from typing import Any, Optional

from Node import Node

class DoubleLinkedNode(Node):
    """Дочерний класс который описывает двусвязный список"""
    def __init__(self, value: Any):
        """
        Инициализация атрибутов класса, super() вызывает конструктор родительского класса
        :param value: Люое значение которое помещено в узел
        """
        super().__init__(value)
        self.next = None
        self.prev = None
