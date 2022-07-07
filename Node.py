from typing import Any, Optional

class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Метод инициализация атрибутов класса
        :param value: Любое значение, которое помещено в узел
        :param next_: Следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __str__(self) -> str: #магический метод для отображения информации об объекте класса для пользователей
        """
        Метод __str__ возвращает строковое представление объекта
        :return: Значение узла и сам узел
        """
        #return str(self.value)
        return f"Node({self.value}, {self.next})"

    def __repr__(self): # магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков)
        """
        Метод __repr__ возвращает печатное представление объекта
        :return: Значение узла и сам узел
        """
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"
        #return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        """
        Метод is_valid проверки на корректность связываемости узла
        :param node:
        :return:
        """
        if not isinstance(node, (type(None), Node)): #проверка node тип None и тип класса Node
            raise TypeError

    @property
    def next(self):
        """
        Декоратор (getter) - метод, получения доступа к атрибуту
        :return:
        """
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        """
        Декоратор (Setter) - метод, изменения/установления значения атрибутов
        :param next_:
        :return:
        """
        self.is_valid(next_)
        self._next = next_

if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.next = node_2
    node_2.next = node_3

    print("вызов метода str")
    print(node_1)
    print(node_2)
    print(node_3)
    print("____________")

    print("вызов метода repr")
    print(repr(node_1))
    print(repr(node_2))
    print(repr(node_3))
