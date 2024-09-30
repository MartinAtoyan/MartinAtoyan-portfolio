

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.height

    @property
    def width(self):
        return self.width

    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be a positive number")

    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            ValueError("Width must be positive number")

    @property
    def area(self):
        return self.__width * self.__height

    @property
    def perimeter(self):
        return (self.__width + self.__height) * 2


# r1 = Rectangle(3, 4)
# print(r1.area)
# print(r1.perimeter)
# r1.width = 7
# r1.height = 12
# print(r1.area)
# print(r1.perimeter)
