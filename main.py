from WindowLogic.Maze import Maze
from WindowLogic.Window import Window
import random

WIDTH = 50 + 100 * 5 + 50
HEIGHT = 800

def main():
    window = Window(WIDTH, HEIGHT)

    # Initialize maze dimensions and parameters
    num_rows, num_cols = 5, 5
    cell_width, cell_height = 100, 100

    # Create a function to initialize and draw the maze with a new seed
    def create_and_draw_maze(seed=None):
        if seed is None:
            seed = random.randint(0, 10000)  # Generate a new seed
        random.seed(seed)  # Set the seed for randomization
        print(f"Using random seed: {seed}")  # Debug info (can be removed)
        maze = Maze(50, 50, num_rows, num_cols, cell_width, cell_height, window, seed)
        maze.break_walls()
        maze.animate()

    # Initial maze generation
    create_and_draw_maze()

    # Function to regenerate the maze
    def regenerate_maze(event):
        window.clear_canvas()  # Clear the canvas
        create_and_draw_maze()  # Generate and draw a new maze

    # Bind the R key to the regeneration function
    window.bind_key("<r>", regenerate_maze)

    window.Wait_for_Close()

if __name__ == '__main__':
    main()
