from WindowLogic.Line import *

class Cell:
    def __init__(self, window, point1, point2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = point1.x # left wall x
        self._y1 = point1.y # top wall y
        self._x2 = point2.x # bottom wall x
        self._y2 = point2.y # right wall y

        self._canvas = window.get_canvas()  # Access the canvas from the Window instance

    def draw(self):
        """Draw the cell based on its walls."""
        if self.has_left_wall:
            self._canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="black", width=2)
        if self.has_right_wall:
            self._canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
        if self.has_top_wall:
            self._canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
        if self.has_bottom_wall:
            self._canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)


    def draw_move(self, move_to_cell, undo=False):
        """Draw a line between two cells."""
        # Calculate center of this cell
        x1_cent = (self._x1 + self._x2) / 2
        y1_cent = (self._y1 + self._y2) / 2

        # Calculate center of the destination cell
        x2_cent = (move_to_cell._x1 + move_to_cell._x2) / 2
        y2_cent = (move_to_cell._y1 + move_to_cell._y2) / 2

        # Color the line based on undo flag
        color = "gray" if undo else "red"

        # Draw the line using the calculated center points
        self._canvas.create_line(x1_cent, y1_cent, x2_cent, y2_cent, fill=color, width=2)
