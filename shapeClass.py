class Shape:
    def __init__(self, area, helef):
        self.__area = area
        self.__helef = helef

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        if value > 0:
            self.__area = value

    @property
    def helef(self):
        return self.__helef

    @helef.setter
    def helef(self, value):
        if value > 0:
            self.__helef = value

    def __str__(self):
        return f"Shape's Details:\nArea: {self.__area}\nHelef: {self.__helef}"

    def __repr__(self):
        return f"Shape({self.__area}, {self.__helef})"
