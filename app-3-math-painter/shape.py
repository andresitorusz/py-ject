class Rectangle:

    def __init__(self, point, width, length, color):
        self.point = point
        self.width = width
        self.length = length
        self.color = color

    def draw(self, canvas):
        pass


class Square:

    def __init__(self, point, side, color):
        self.point = point
        self.side = side
        self.color = color

    def draw(self, canvas):
        pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
