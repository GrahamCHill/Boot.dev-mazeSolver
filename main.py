from WindowLogic.Window import Window

WIDTH = 800
HEIGHT = 600

def main():
    var = Window(WIDTH, HEIGHT)
    var.tk_canvas.mainloop()

if __name__ == '__main__':
    main()
