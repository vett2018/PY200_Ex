from typing import Any, Optional, Iterable
from collections.abc import MutableSequence

from node_and_doublenode import Node


class LinkedList(MutableSequence):
    """Класс который описывает односвязный список"""
    def __init__(self, data: Iterable = None):
        """
        Метод инициализации атрибутов класса
        :param data: данные для добавления в список
        """
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head
        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """
        Метод возвращение элемента по индексу
        :param index: Индес элемента
        :return: Значение элемента по индексу
        """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def append(self, value: Any):
        """
        Добавление элмента в конец списка
        :param value: Значение которое будет вставлено
        """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        # left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """
        Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел.
        :param index: Индекс узла
        :return: Текущий узел
        """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:
            raise IndexError("Значение индекса меньше 0 или больше длины списка")

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def insert(self, index: int, value: Any) -> None:
        """
        Метод вставки узла по указанному индексу
        :param index: Индекс элемента
        :param value: Значение элемента
        :return: Связный список
        """
        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1

    def __delitem__(self, index: int):
        """
        Удалление узла по индексу
        :param index: Индекс удаляемого элемента
        :return:
        """
        node = self.step_by_step_on_nodes(index)
        node.value = None

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Метод установки значения узла по указанному индексу
        :param index: Индекс жлемента
        :param value: Значение элемента
        :return: Связный список
        """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __len__(self) -> int:
        """
        Метод подсчета длины связного списка
        :return: Колличество узлов
        """
        return self._len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __str__(self) -> str:
        """ """
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        # return f"{self.__class__.__name__}({self.to_list()})"
        return f"{self.__class__.__name__} {self.to_list()}"

if __name__ == "__main__":
    ll = LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("________________")
    print("Вывод листа - метод str:")
    print(str(ll))
    print("________________")
    print("Вывод листа - метод repr:")
    print(repr(ll))
    print("________________")
    print("Вывод длины листа:")
    print(ll._len)
    print("________________")
    print("Вставка элемента по индексу:")
    ll.insert(5, 33333)
    print(repr(ll))
    print("________________")
    print("Вставка значения в конец списка:")
    ll.append(4444)
    print(repr(ll))
    print("________________")
    print("вставка элемента по индексу метод setitem")
    ll.__setitem__(1, 888)
    print(repr(ll))
    print("________________")
    print(f"Вывод элемента по индексу 1 - метод gettitem = {ll.__getitem__(1)}")

