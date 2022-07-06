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

    def __str__(self) -> str:
        """
        Метод __str__ возвращает строковое представление объекта
        :return: Значение узла и сам узел
        """
        return f"Node({self.value}, {self.next})"

    def __repr__(self):
        """
        Метод __repr__ возвращает печатное представление объекта
        :return: Значение узла и сам узел
        """
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        """
        Метод is_valid проверки на корректность связываемости узла
        :param node:
        :return:
        """
        def is_valid(self, node: Any) -> None:
            if not isinstance(node, (type(None), Node)):
                raise TypeError


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.next = node_2
    node_2.next = node_3

    print(node_1)
    print(node_2)
    print(node_3)

