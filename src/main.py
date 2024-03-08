from window import Window
from shapes import Line, Point
from maze import Maze

def main():
    win = Window(800,600)

    print(f"{win.width}, {win.height}")
    maze = Maze(10, 12, win)
    

    print(f"{win.width}, {win.height}")
    win.wait_for_close()

main()
