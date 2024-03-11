from window import Window
from shapes import Line, Point
from maze import Maze

def main():
    win = Window(800,1440)

    maze = Maze(20, 30, win)
    maze.solve()

    win.wait_for_close()

main()
