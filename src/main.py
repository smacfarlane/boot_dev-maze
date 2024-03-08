from window import Window
from shapes import Line, Point
from cell import Cell

def main():
    win = Window(800,600)

    cell = Cell(Point(0,0), win)
    cell.draw()

    cell2 = Cell(Point(10,0), win)
    cell2.draw()

    cell3 = Cell(Point(0,10), win)
    cell3.draw()

    cell.draw_move(cell2)
    cell2.draw_move(cell3, True)

    win.wait_for_close()

main()
