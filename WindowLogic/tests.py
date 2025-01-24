import unittest
from WindowLogic.Maze import Maze
from WindowLogic.Window import Window


class MazeTests(unittest.TestCase):
    def setUp(self):
        """Set up a dummy window and maze instance for testing."""
        self.num_cols = 5
        self.num_rows = 4
        self.cell_size_x = 20
        self.cell_size_y = 20
        self.win = Window(0, 0)
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self.win)


    def test_maze_dimensions(self):
        self.assertEqual(len(self.maze._cells), self.num_rows, "Number of rows does not match")
        for row in self.maze._cells:
            self.assertEqual(len(row), self.num_cols, "Number of columns in row does not match")


    def test_cell_wall_defaults(self):
        """Test that the maze cells have the correct default walls."""
        for i, row in enumerate(self.maze._cells):
            for j, cell in enumerate(row):
                if i == 0 and j == 0:  # Entry cell (top-left corner)
                    # Only one wall should be removed from the entry
                    self.assertTrue(cell.has_left_wall or cell.has_top_wall,
                                    "Expected left or top wall to be intact on entry cell")
                    self.assertFalse(cell.has_left_wall and cell.has_top_wall,
                                     "Expected only one of the left or top wall to be removed")
                    self.assertTrue(cell.has_right_wall, "Expected right wall to be True on entry cell")
                    self.assertTrue(cell.has_bottom_wall, "Expected bottom wall to be True on entry cell")
                elif i == self.maze.num_rows - 1 and j == self.maze.num_cols - 1:  # Exit cell (bottom-right corner)
                    # Only one wall should be removed from the exit
                    self.assertTrue(cell.has_right_wall or cell.has_bottom_wall,
                                    "Expected right or bottom wall to be intact on exit cell")
                    self.assertFalse(cell.has_right_wall and cell.has_bottom_wall,
                                     "Expected only one of the right or bottom wall to be removed")
                    self.assertTrue(cell.has_left_wall, "Expected left wall to be True on exit cell")
                    self.assertTrue(cell.has_top_wall, "Expected top wall to be True on exit cell")
                else:  # All other cells should have all walls intact
                    self.assertTrue(cell.has_top_wall, "Expected top wall to be True")
                    self.assertTrue(cell.has_left_wall, "Expected left wall to be True")
                    self.assertTrue(cell.has_right_wall, "Expected right wall to be True")
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


    def test_reset_cells_visited(self):
        """Test that `_reset_cells_visited` sets all cell visited flags to False."""
        # Create a small maze for testing
        window = Window(300, 300)
        maze = Maze(0, 0, 3, 3, 100, 100, window, 42)

        # Simulate visiting cells
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):
                maze._cells[i][j].visited = True  # Set all cells to visited

        # Call the method to reset visited flags
        maze._reset_cells_visited()

        # Assert all cells are reset to not visited
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):
                self.assertFalse(maze._cells[i][j].visited, f"Cell ({i}, {j}) should not be visited.")


if __name__ == "__main__":
    unittest.main()
