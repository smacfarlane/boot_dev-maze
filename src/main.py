from window import Window
from shapes import Line, Point

def main():
    win = Window(800,600)
    line = Line(Point(0,0),Point(200, 200))
    win.draw_line(line, "blue")
    win.wait_for_close()

main()
