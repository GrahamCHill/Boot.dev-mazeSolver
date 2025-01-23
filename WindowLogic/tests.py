import unittest
from WindowLogic.Maze import Maze
from WindowLogic.Cell import Cell
from WindowLogic.Window import Window
from WindowLogic.Point import Point
import time

class MazeTests(unittest.TestCase):
    def setUp(self):
        """Set up a dummy window and maze instance for testing."""
        self.num_cols = 5
        self.num_rows = 4
        self.cell_size_x = 20
        self.cell_size_y = 20
        self.win = Window(800, 800)
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.win)

    def test_maze_dimensions(self):
        self.assertEqual(len(self.maze._cells), self.num_rows, "Number of rows does not match")
        for row in self.maze._cells:
            self.assertEqual(len(row), self.num_cols, "Number of columns in row does not match")

    def test_cell_wall_defaults(self):
        for row in self.maze._cells:
            for cell in row:
                self.assertTrue(cell.has_left_wall, "Expected left wall to be True")
                self.assertTrue(cell.has_right_wall, "Expected right wall to be True")
                self.assertTrue(cell.has_top_wall, "Expected top wall to be True")
                self.assertTrue(cell.has_bottom_wall, "Expected bottom wall to be True")

    def test_draw_cells(self):
        try:
            for row in self.maze._cells:
                for cell in row:
                    cell.draw()
        except Exception as e:
            self.fail(f"Cell drawing raised an exception: {e}")

    def test_maze_animation(self):
        try:
            self.maze.animate()
        except Exception as e:
            self.fail(f"Maze animation raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
