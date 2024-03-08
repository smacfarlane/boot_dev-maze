import random
import time

from cell import Cell, Wall
from shapes import Point


class Maze:
    def __init__(self, rows: int, cols: int, win=None):
        self._rows = rows
        self._cols = cols
        self._cells = []
        self.__visited = set()
        self.__win = win
        self.__create_cells()

    def __create_cells(self):
        for j in range(self._rows):
            row = []
            for i in range(self._cols):
                row.append(Cell(Point(i,j), self.__win))
            self._cells.append(row)
        
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

        for i in range(self._rows):
            for j in range(self._cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
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

    def __break_walls_r(self, i: int, j: int):
        self.__visited.add((i, j))
        while True:
            adjacent = []

            if i != 0 and (i-1, j) not in self.__visited:
                adjacent.append(((i-1, j), Wall.TOP))
            if i < self._rows -1 and (i+1, j) not in self.__visited:
                adjacent.append(((i+1, j), Wall.BOTTOM))
            if j != 0 and (i, j-1) not in self.__visited:
                adjacent.append(((i, j-1), Wall.LEFT))
            if j < self._cols -1 and (i, j+1) not in self.__visited:
                adjacent.append(((i, j+1), Wall.RIGHT))

            if len(adjacent) == 0:
                self.__draw_cell(i,j)
                return
            
            direction = random.randint(0,len(adjacent)-1)

            (neighbor, wall) = adjacent[direction]

            self._cells[i][j].has_wall(wall, False)
            self._cells[neighbor[0]][neighbor[1]].has_wall(wall.opposite(), False)

            self.__break_walls_r(neighbor[0], neighbor[1])

            






