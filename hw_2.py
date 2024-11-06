
class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Square side length: {self.__side_length} cm, area: {self.calculate_area()} cm')

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length} cm, width: {self.__width} cm,'
              f' area: {self.calculate_area ()} cm')

figures = [
    Square(6),
    Square(11),
    Rectangle(6,4),
    Rectangle(9, 7),
    Rectangle(3,1)
]

for figure in figures:
    figure.info()


