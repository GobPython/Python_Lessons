# Домашнее задание после Урока 34
# Добавить абстрактный класс Animal и переопределить в нём все будущие абстрактные методы.
from abc import abstractmethod
class Animal:
    def __init__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def size(self):
        pass
