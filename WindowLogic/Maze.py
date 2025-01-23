import time

from WindowLogic.Cell import Cell
from WindowLogic.Point import Point


class Maze:
    def __init__(self, x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._create_cells()


    def _create_cells(self):
        for y in range(self.num_rows):
            column = []
            for x in range(self.num_cols):
                point1 = Point(
                    self.x1 + y * self.cell_size_x,
                    self.y1 + x * self.cell_size_y,
                )
                point2 = Point(
                    point1.x + self.cell_size_x,
                    point1.y + self.cell_size_y,
                )

                cell = Cell(self._win, point1, point2)
                column.append(cell)
                self._draw_cell(cell)
            self._cells.append(column)


    def _draw_cell(self, cell):
        cell.draw()
        self.animate()
        pass


    def animate(self):
        self._win.Redraw()
        time.sleep(0.05)