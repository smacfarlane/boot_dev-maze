from window import Window
from shapes import Line, Point
from cell import Cell

def main():
    win = Window(800,600)

    cell = Cell(Point(0,0), win)
    cell.draw()

    cell = Cell(Point(10,0), win)
    cell.draw()

    cell.draw(50)

    cell = Cell(Point(10, 10), win)
    cell.draw()

    cell = Cell(Point(20, 20), win)
    cell.has_top(False)
    cell.has_bottom(False)

    cell.draw()

    win.wait_for_close()

main()
