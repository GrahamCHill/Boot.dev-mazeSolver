import time
import random

from WindowLogic.Cell import Cell
from WindowLogic.Line import Line
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

        # To prevent multiple solvings at the same time
        self._is_solving = False


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
        time.sleep(0.00125)


    def _reset_cells_visited(self):
        """Reset the `visited` property of all cells in the maze to False."""
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        """Solve the maze."""
        print("Solving...")
        self._reset_cells_visited()  # Reset all cells' visited status
        if self._solve_r(0, 0):
            print("Solved!")
        else:
            print("No solution found.")

    def _solve_r(self, i, j):
        """Recursive maze-solving logic with proper animation."""
        # Check if the current cell is out of bounds
        if i < 0 or i >= self.num_rows or j < 0 or j >= self.num_cols:
            return False

        cell = self._cells[i][j]

        # Check if the cell is already visited
        if cell.visited:
            return False

        # Mark the cell as visited
        cell.visited = True

        # Base case: if the cell is the exit, maze is solved
        if cell == self.exit:
            return True

        # Directions: Down, Right, Up, Left
        directions = [
            (1, 0, "has_bottom_wall", "has_top_wall"),  # Down
            (0, 1, "has_right_wall", "has_left_wall"),  # Right
            (-1, 0, "has_top_wall", "has_bottom_wall"),  # Up
            (0, -1, "has_left_wall", "has_right_wall"),  # Left
        ]

        for di, dj, current_wall, next_wall in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < self.num_rows and 0 <= nj < self.num_cols:
                next_cell = self._cells[ni][nj]

                # Check if there's a wall between the current cell and the next cell
                if not getattr(cell, current_wall) and not getattr(next_cell, next_wall):
                    # Draw a red line to the next cell
                    cell.draw_move(next_cell)
                    self.animate()  # Ensure animation for visualization

                    # Recursive call
                    if self._solve_r(ni, nj):
                        return True

                    # Undo move with a gray line if the path is invalid (backtrack)
                    cell.draw_move(next_cell, undo=True)
                    self.animate()  # Animate the undo operation

        # Backtrack if no valid path is found
        return False




