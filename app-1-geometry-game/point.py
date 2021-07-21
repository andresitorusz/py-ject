import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < rectangle.point2.x:
            if rectangle.point1.y < rectangle.point2.y:
                if rectangle.point1.x < self.x \
                        < rectangle.point2.x \
                        and rectangle.point1.y < self.y \
                        < rectangle.point2.y:
                    return True
                else:
                    return False
            else:
                if rectangle.point1.x < self.x \
                        < rectangle.point2.x \
                        and rectangle.point1.y > self.y \
                        > rectangle.point2.y:
                    return True
                else:
                    return False
        else:
            if rectangle.point1.y < rectangle.point2.y:
                if rectangle.point1.x > self.x \
                        > rectangle.point2.x \
                        and rectangle.point1.y < self.y \
                        < rectangle.point2.y:
                    return True
                else:
                    return False
            else:
                if rectangle.point1.x > self.x \
                        > rectangle.point2.x \
                        and rectangle.point1.y > self.y \
                        > rectangle.point2.y:
                    return True
                else:
                    return False


class PointGUI(Point):

    def draw(self, canvas, size=2.5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

        turtle.done()
