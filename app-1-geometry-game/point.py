class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x \
                < rectangle.point2.x \
                and rectangle.point1.y < self.y \
                < rectangle.point2.y:
            return True
        else:
            return False
