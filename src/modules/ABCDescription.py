from abc import ABC


class ABCDescription(ABC):
    def __init__(self, name, desc):
        self._name = name
        self._desc = desc

    def get_name(self):
        return self._name

    def get_desc(self):
        return self._desc
