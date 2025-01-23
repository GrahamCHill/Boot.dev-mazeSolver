import unittest
from WindowLogic.Maze import Maze
from WindowLogic.Window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10

        # Create a dummy window object to pass into Maze
        win = Window(300, 300)

        # Create the Maze instance
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y, win)

        # Check that there are `num_rows` rows
        self.assertEqual(len(m1._cells), num_rows, "Number of rows does not match")

        # Check that each row contains `num_cols` cells
        for row in m1._cells:
            self.assertEqual(len(row), num_cols, "Number of columns in row does not match")

if __name__ == "__main__":
    unittest.main()
