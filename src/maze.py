import time
from cell import Cell
from shapes import Point


class Maze:
    def __init__(self, rows, cols, win=None):
        self._rows = rows
        self._cols = cols
        self._cells = []
        self.__win = win
        self.__create_cells()

    def __create_cells(self):
        for j in range(self._rows):
            row = []
            for i in range(self._cols):
                row.append(Cell(Point(i,j), self.__win))
            self._cells.append(row)
        
        print(f"R: {len(self._cells)}")
        print(f"C: {len(self._cells[0])}")

        self.__break_entrance_and_exit()

        for i in range(self._rows):
            for j in range(self._cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        print(f"{i},{j}: {self._cells[i][j]}")
        self._cells[i][j].draw()
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.1)

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top(False)
        self._cells[self._rows-1][self._cols-1].has_bottom(False)

        self.__draw_cell(0,0)
        self.__draw_cell(self._rows-1, self._cols-1)




