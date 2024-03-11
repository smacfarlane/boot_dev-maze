from tkinter import Tk, BOTH, Canvas
from shapes import Line, Point

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Boot.dev Maze")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.__canvas = Canvas()
        self.__canvas.pack(expand=1, fill='both', padx=5, pady=5)

        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, color: str):
        line.draw(self.__canvas, color)

    def draw_point(self, point: Point, color: str):
        point.draw(self.__canvas, color)





