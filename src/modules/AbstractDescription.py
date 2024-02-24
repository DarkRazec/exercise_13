from abc import ABC, abstractmethod


class AbstractDescription(ABC):
    """Абстрактный класс для класса Category и Product"""
    def __init__(self, name, desc):
        self._name = name
        self._desc = desc

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def get_name(self):
        return self._name

    def get_desc(self):
        return self._desc
