from WindowLogic.Cell import Cell
from WindowLogic.Line import Line
from WindowLogic.Point import Point
from WindowLogic.Window import Window

WIDTH = 800
HEIGHT = 800

def main():
    window = Window(WIDTH, HEIGHT)

    cell1 = Cell(window, Point(50, 50), Point(150, 150))
    cell1.has_right_wall = False
    cell2 = Cell(window, Point(200, 50), Point(300, 150))
    cell2.has_left_wall = False

    # Draw the cells
    cell1.draw()
    cell2.draw()

    # Draw a move path from cell1 to cell2
    cell1.draw_move(cell2, undo=False)  # Red line for forward move

    # Simulate an undo move (gray line)
    # cell2.draw_move(cell1, undo=True)


    window.Wait_for_Close()

if __name__ == '__main__':
    main()
