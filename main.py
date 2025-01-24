from WindowLogic.Maze import Maze
from WindowLogic.Window import Window
import random

WIDTH = 50 + 100 * 5 + 50
HEIGHT = 800

def main():
    def regenerate_maze(event):
        """Regenerate the maze."""
        global maze
        window.clear_canvas()
        maze = Maze(50, 100, 30, 30, 20, 20, window)
        maze.break_walls()

    def solve_maze(event):
        """Solve the maze."""
        maze.solve()

    def regenerate_and_solve_maze(event):
        """Regenerate the maze and solve it."""
        regenerate_maze(event)
        maze.solve()

    # Initialize the window and maze
    window = Window(800, 800)
    # maze = Maze(50, 50, 10, 10, 40, 40, window)
    # maze.break_walls()
    regenerate_maze(window) # Initial Generation
    # Bind keys
    window.bind_key("<r>", regenerate_maze)  # Regenerate maze
    window.bind_key("<e>", solve_maze)  # Solve maze
    window.bind_key("<Shift-R>", regenerate_and_solve_maze)  # Regenerate and solve maze

    # Run the application
    window.Wait_for_Close()


if __name__ == '__main__':
    main()
