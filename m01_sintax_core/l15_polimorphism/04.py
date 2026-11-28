# Фигуры.

# Создайте базовый класс Shape, который будет иметь метод area для вычисления площади.
# Затем создайте два дочерних класса Rectangle и Circle, которые будут наследовать от Shape
# и переопределять метод area для вычисления площади прямоугольника и круга соответственно.

import math


class Shape:
    def area(self, a, b):
        return a ** a + b ** b


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(5, 3)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(4)
print(f"Area of circle: {circle.area()}")
