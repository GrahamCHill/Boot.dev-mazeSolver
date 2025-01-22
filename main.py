from WindowLogic.Line import Line
from WindowLogic.Point import Point
from WindowLogic.Window import Window

WIDTH = 800
HEIGHT = 800

def main():
    var = Window(WIDTH, HEIGHT)
    point1 = Point(0, 0)
    point2 = Point(50, 350)
    point3 = Point(200, 550)

    line1 = Line(point1, point2)
    line2 = Line(point1, point3)
    line3 = Line(point3, point1)

    var.draw_line(line1, "red")
    var.draw_line(line2, "blue")
    var.draw_line(line3, "green")

    var.Wait_for_Close()

if __name__ == '__main__':
    main()
