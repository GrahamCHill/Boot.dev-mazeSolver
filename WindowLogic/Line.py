from WindowLogic.Point import *

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1  # First endpoint (Point instance)
        self.point2 = point2  # Second endpoint (Point instance)


    def draw(self, canvas, fill_color):
        """Draw the line on the canvas."""
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=4
        )


