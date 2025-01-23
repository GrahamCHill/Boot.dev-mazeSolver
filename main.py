from WindowLogic.Maze import Maze
from WindowLogic.Window import Window

WIDTH = 50 + 100 * 5 + 50
HEIGHT = 800

def main():
    window = Window(WIDTH, HEIGHT)

    # Create a maze with 5 rows and 5 columns, starting at (50, 50)
    maze = Maze(50, 50, 5, 5, 100, 100, window, 2)

    print(maze.entry)
    print(maze.exit)
    print( maze._cells)
    window.Wait_for_Close()

if __name__ == '__main__':
    main()
