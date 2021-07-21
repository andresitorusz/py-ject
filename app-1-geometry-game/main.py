from random import randint
from point import PointGUI
from rectangle import RectangleGUI
from colorama import Fore
from turtle import Turtle


def main():
    rectangle = RectangleGUI(
        PointGUI(randint(10, 100), randint(10, 100)),
        PointGUI(randint(20, 100), randint(20, 100))
    )

    print("Rectangle Coordinates: {0}, {1} and {2}, {3}"
          .format(rectangle.point1.x, rectangle.point1.y,
                  rectangle.point2.x, rectangle.point2.y))

    rectangle_turtle = Turtle()
    user_point = guess(rectangle=rectangle)
    rectangle.draw(canvas=rectangle_turtle)
    user_point.draw(canvas=rectangle_turtle)


def guess(rectangle):
    user_point = PointGUI(float(input("Guess X: ")),
                          float(input("Guess Y: ")))
    user_area = float(input("Guess rectangle area: "))

    if user_point.falls_in_rectangle(rectangle):
        print(Fore.GREEN + "Your point ({0}, {1}) was inside rectangle."
              .format(int(user_point.x), int(user_point.y)))
    else:
        print(Fore.RED + "Your point ({0}, {1}) was outside rectangle."
              .format(int(user_point.x), int(user_point.y)))

    if user_area == rectangle.area():
        print(Fore.GREEN + "Great! Your area guess was true. The area is {}."
              .format(rectangle.area()))
    else:
        print(Fore.RED + "Wrong area guess! The area is {}."
              .format(rectangle.area()))

    return user_point


if __name__ == '__main__':
    main()
