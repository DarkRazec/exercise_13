class MixinRepr:
    """Класс для вывода в консоль информации о том, что был создан объект какого-либо класса"""
    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"
