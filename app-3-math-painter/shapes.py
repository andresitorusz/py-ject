class Rectangle:
    """
    A rectangle shape that can be drawn on a Canvas object
    """

    def __init__(self, point, width, length, color):
        self.point = point
        self.width = width
        self.length = length
        self.color = color

    def draw(self, canvas):
        canvas.data[self.point.x: self.point.x + self.length, self.point.y: self.point.y + self.width] = self.color


class Square:
    """
    A square shape that can be drawn on a Canvas object
    """

    def __init__(self, point, side, color):
        self.point = point
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.point.x: self.point.x + self.side, self.point.y: self.point.y + self.side] = self.color


class Point:
    """
    A starting point of a shape
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
