from abc import ABC, abstractmethod


class AbstractDescription(ABC):
    """Абстрактный класс для класса 'Category' и 'Product'"""
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

    def get_name(self):
        """Возвращает значение поля _name"""
        return self._name

    def get_desc(self):
        """Возвращает значение поля _desc"""
        return self._desc
