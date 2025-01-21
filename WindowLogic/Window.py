from tkinter import *


class Window:
    def __init__(self, width, height):
        self.width = None
        self.height = None
        self.window = Tk()
        self.window.title("Python Maze Generator and Solver")
        self.window.geometry(f"{width}x{height}")

        self.tk_canvas = Canvas(self.window)
        self.tk_canvas.pack()

        self.tk_running = False


    def Window(self, width, height):
        self.__init__(width, height)
