from typing import Any, Optional

class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any):
        """
        Инициализация атрибутов класса
        :param value:
        Метод инициализация атрибутов класса
        :param value: Любое значение, которое помещено в узел
        """
        self.value = value
        self.next = None

    def __str__(self):
    def __str__(self) -> str:
        """
        Метод __str__ сроковое представление объекта
        :return: Значение узла и сам узел
        """
        return f"Значение строковой версии объекта = {self.value}, {self.next}"

    def __repr__(self):
        """
        Метод __repr__ сроковое представление объекта
        :return: Значение узла и сам узел
        """
        return f"Значение печатной версии объекта = {self.value}, {self.next}"

    def is_valid(self, node: Any) -> None:
        """
        Метод is_valid
        :param node:
        :return:
        """
        return


    def __repr__(self):
        ...


class DoubleLinkedNode(Node):