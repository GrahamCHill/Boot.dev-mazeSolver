from WindowLogic.Window import Window

WIDTH = 800
HEIGHT = 600

def main():
    var = Window(WIDTH, HEIGHT)
    var.Wait_for_Close()

if __name__ == '__main__':
    main()
