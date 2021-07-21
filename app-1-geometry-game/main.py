from random import randint
from point import Point
from rectangle import Rectangle


def main():
    rectangle = Rectangle(
        Point(randint(0, 9), randint(0, 9)),
        Point(randint(10, 19), randint(10, 19))
    )

    print("Rectangle Coordinates: {0}, {1} and {2}, {3}"
          .format(rectangle.point1.x, rectangle.point1.y,
                  rectangle.point2.x, rectangle.point2.y))

    guess(rectangle)


def guess(rectangle):
    user_point = Point(float(input("Guess X: ")),
                       float(input("Guess Y: ")))
    user_area = float(input("Guess rectangle area: "))

    if user_point.falls_in_rectangle(rectangle):
        print("Your point was inside rectangle.")
    else:
        print("Your point was outside rectangle.")

    if user_area == rectangle.area():
        print("Great! Your area guess was true. The area is {}."
              .format(rectangle.area()))
    else:
        print("Wrong area guess! The area is {}."
              .format(rectangle.area()))


if __name__ == '__main__':
    main()