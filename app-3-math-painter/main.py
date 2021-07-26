from colorama import Fore
from canvas import Canvas
from shapes import Rectangle, Square, Point


def main():
    print(Fore.GREEN + "Hello there! Welcome to math painter application." + Fore.RESET)
    canvas = create_canvas()

    while True:
        shape_type = input("What do you like to draw? ")

        if shape_type.lower() == "rectangle":
            rec_point = Point(int(input("Enter x of the rectangle: ")),
                              int(input("Enter y of the rectangle: ")))
            rec_width = int(input("Enter the width of the rectangle: "))
            rec_length = int(input("Enter the length of the rectangle: "))
            red = int(input("How much red should the rectangle have? "))
            green = int(input("How much green? "))
            blue = int(input("How much blue? "))

            rec = Rectangle(point=rec_point, width=rec_width, length=rec_length, color=(red, green, blue))
            rec.draw(canvas=canvas)

        if shape_type.lower() == "square":
            sq_point = Point(int(input("Enter x of the square: ")),
                             int(input("Enter y of the square: ")))
            sq_side = int(input("Enter the side lenght of the square: "))
            red = int(input("How much red should the rectangle have? "))
            green = int(input("How much green? "))
            blue = int(input("How much blue? "))

            sq = Square(point=sq_point, side=sq_side, color=(red, green, blue))
            sq.draw(canvas=canvas)

        if shape_type == "quit":
            break

    canvas.make('output/canvas.png')


def create_canvas():
    canvas_width = int(input("Enter canvas width: "))
    canvas_lenght = int(input("Enter canvas lenght: "))

    colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
    canvas_color = input("Enter canvas color (white or black): ")

    canvas = Canvas(width=canvas_width, length=canvas_lenght, color=colors[canvas_color])

    return canvas


if __name__ == '__main__':
    main()
