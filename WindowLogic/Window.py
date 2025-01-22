from tkinter import *
from WindowLogic.Line import *

class Window:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__window = Tk()
        self.__window.title("Python Maze Generator and Solver")
        self.__window.geometry(f"{width}x{height}")


        self.__tk_canvas = Canvas(self.__window, width=width, height=height, background="white")
        self.__tk_canvas.pack()

        self.__tk_running = False

        self.__window.protocol("WM_DELETE_WINDOW", self.Close)


    def Window(self, width, height):
        self.__init__(width, height)

    def get_canvas(self):
        """Provide access to the canvas."""
        return self.__tk_canvas

    def Redraw(self):
        self.__window.update_idletasks()
        self.__window.update()


    def Wait_for_Close(self):
        self.__tk_running = True
        try:
            while self.__tk_running:
                self.Redraw()
        except TclError:
            # Catch errors if the window is already destroyed
            self.__tk_running = False


    def Close(self):
        self.__tk_running = False
        self.__window.destroy()


    def draw_line(self, line, fill_color):
        """Draw a Line instance on the canvas."""
        line.draw(self.__tk_canvas, fill_color)