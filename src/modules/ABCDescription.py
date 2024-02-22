from abc import ABC, abstractmethod


class ABCDescription(ABC):
    """Абстрактный класс для класса Category и Product"""
    name: str
    desc: str

    def __init__(self, name: str, desc: str):
        self._name = name
        self._desc = desc

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    def get_name(self):
        """Возвращает значение поля 'name'"""
        return self._name

    def get_desc(self):
        """Возвращает значение поля 'desc'"""
        return self._desc
