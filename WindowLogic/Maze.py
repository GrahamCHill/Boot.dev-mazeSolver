import time
import random

from WindowLogic.Cell import Cell
from WindowLogic.Point import Point


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, r_seed=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        # Random seed for reproducibility
        if r_seed is not None:
            random.seed(r_seed)

        # Entry and exit points
        self.entry = None
        self.exit = None

        self._create_cells()

    def _create_cells(self):
        """Create all the cells and set the entry and exit points."""
        for y in range(self.num_rows):
            row = []
            for x in range(self.num_cols):
                point1 = Point(self.x1 + x * self.cell_size_x, self.y1 + y * self.cell_size_y)
                point2 = Point(point1.x + self.cell_size_x, point1.y + self.cell_size_y)
                row.append(Cell(self._win, point1, point2))
            self._cells.append(row)

        # Set entry and exit points (top-left and bottom-right corners)
        self.entry = self._cells[0][0]  # Top-left corner
        self.exit = self._cells[self.num_rows - 1][self.num_cols - 1]  # Bottom-right corner

        # Remove walls at the entry and exit points
        self.entry.has_top_wall = False
        self.exit.has_bottom_wall = False

    def break_walls(self):
        """Start the maze generation process."""
        self._generate_maze(0, 0)  # Start from the entry cell
        self._ensure_outer_walls()

    def _generate_maze(self, i, j):
        """Generate the maze using Depth-First Search (DFS) and backtracking."""
        self._cells[i][j].visited = True
        directions = [
            (-1, 0, "top", "bottom"),  # Up
            (1, 0, "bottom", "top"),  # Down
            (0, -1, "left", "right"),  # Left
            (0, 1, "right", "left"),  # Right
        ]
        random.shuffle(directions)

        for di, dj, current_wall, neighbor_wall in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.num_rows and 0 <= nj < self.num_cols and not self._cells[ni][nj].visited:
                # Remove walls between current cell and neighbor
                setattr(self._cells[i][j], f"has_{current_wall}_wall", False)
                setattr(self._cells[ni][nj], f"has_{neighbor_wall}_wall", False)

                # Redraw cells
                self._cells[i][j].draw()
                self._cells[ni][nj].draw()
                self.animate()

                # Recursively visit the neighbor
                self._generate_maze(ni, nj)

    def _ensure_outer_walls(self):
        """Ensure all outer walls remain intact except at the entry and exit points."""
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = self._cells[i][j]

                # Top row
                if i == 0 and cell != self.entry:
                    cell.has_top_wall = True
                # Bottom row
                if i == self.num_rows - 1 and cell != self.exit:
                    cell.has_bottom_wall = True
                # Left column
                if j == 0 and cell != self.entry:
                    cell.has_left_wall = True
                # Right column
                if j == self.num_cols - 1 and cell != self.exit:
                    cell.has_right_wall = True

                # Redraw cell to reflect changes
                cell.draw()

    def animate(self):
        """Redraw the canvas with a slight delay for visualization."""
        self._win.Redraw()
        time.sleep(0.05)
