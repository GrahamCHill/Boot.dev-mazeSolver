import time
import random

from WindowLogic.Cell import Cell
from WindowLogic.Point import Point


class Maze:
    def __init__(self, x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win, r_seed = None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        # Generating a random seed value or Default to None if there is none
        if r_seed is not None:
            random.seed(r_seed)
            self._seed = random.randint(1,2)
        else:
            self._seed = 0

        # Track Entry and exit positions
        self.entry = None
        self.exit = None

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
                self._break_entrance_and_exit(cell, x, y, self.num_rows, self.num_cols)
                self._draw_cell(cell)
            self._cells.append(column)


    def _draw_cell(self, cell):
        cell.draw()
        self.animate()
        pass


    def animate(self):
        self._win.Redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self, cell, row, column, row_max, col_max):
        print (self._seed)
        if row == 0 and column == 0:
            if self._seed % 2 == 0:
                cell.has_bottom_wall = False
                cell.has_right_wall_wall = False
                cell.has_top_wall = False
                self.entry = [cell, "top"]
            else:
                cell.has_right_wall = False
                cell.has_bottom_wall = False
                cell.has_left_wall = False
                self.entry = [cell, "left"]
        if row == (row_max - 1) and column == (col_max - 1):
            if self._seed % 2 == 0:
                cell.has_top_wall = False
                cell.has_left_wall = False
                cell.has_bottom_wall = False
                self.exit = [cell, "bottom"]
            else:
                cell.has_left_wall = False
                cell.has_top_wall = False
                cell.has_right_wall = False
                self.exit = [cell, "right"]


    def break_walls(self):
        for cell in self._cells:
            # Prevent the top from losing their border
            if cell._x1 == 0 and self.entry[0]:
                cell.has_top_wall = True
            if cell._y1 == 0 and self.entry[0]:
                cell.has_left_wall = True
            # columns [[col1][col2][col3]...[coln]]
            # right wall
            if cell._x2 == self._cells and cell != self.exit[0]:
                cell.has_right_wall = True
            # bottom wall
            if cell._y2 == self._cells[0] and cell != self.exit[0]:
                cell.has_bottom_wall_wall = True
        pass