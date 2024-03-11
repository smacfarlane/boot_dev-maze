import random
import time

from cell import Cell, Wall
from shapes import Point


class Maze:
    def __init__(self, rows: int, cols: int, win=None):
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
        
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

        for i in range(self._rows):
            for j in range(self._cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        if self.__win is None:
            return
        self._cells[i][j].draw()
        self.__animate()

    def __draw_path(self, a, b, undo=False): 
        a = self._cells[a[0]][a[1]]
        b = self._cells[b[0]][b[1]]

        a.draw_move(b, undo)

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top(False)
        self._cells[self._rows-1][self._cols-1].has_bottom(False)

    def __break_walls_r(self, i: int, j: int, visited=set()):
        visited.add((i, j))
        while True:
            adjacent = []

            if i != 0 and (i-1, j) not in visited:
                adjacent.append(((i-1, j), Wall.TOP))
            if i < self._rows -1 and (i+1, j) not in visited:
                adjacent.append(((i+1, j), Wall.BOTTOM))
            if j != 0 and (i, j-1) not in visited:
                adjacent.append(((i, j-1), Wall.LEFT))
            if j < self._cols -1 and (i, j+1) not in visited:
                adjacent.append(((i, j+1), Wall.RIGHT))

            if len(adjacent) == 0:
                self.__draw_cell(i,j)
                return
            
            direction = random.randint(0,len(adjacent)-1)

            (neighbor, wall) = adjacent[direction]

            self.__break_wall((i,j),neighbor, wall)

            self.__break_walls_r(neighbor[0], neighbor[1], visited)

    def __break_wall(self, a, b, wall):
        a_i, a_j = a
        b_i, b_j = b
        self._cells[a_i][a_j].has_wall(wall, False)
        self._cells[b_i][b_j].has_wall(wall.opposite(), False)

    # Non recursive solution
    # Some non-intuitive tracking required to ensure drawing is done correctly
    def solve(self):
        worklist = [(0,0)]
        visited = set()
        prev = []

        print("---- Solve ----")
        while worklist:
            current = worklist.pop()
            i,j = current

            if len(prev) != 0:
                self.__draw_path(current, prev[-1])

            if current == (self._rows-1, self._cols-1):
                break

            visited.add(current)
            neighbors = []
            
            if( i != 0 and (i - 1, j) not in visited and self.is_connected(i, j, Wall.TOP)):
                neighbors.append((i-1, j))
            if i < self._rows - 1 and (i + 1, j) not in visited and self.is_connected(i, j, Wall.BOTTOM):
                neighbors.append((i + 1, j))
            if j != 0 and (i, j - 1) not in visited and self.is_connected(i, j, Wall.LEFT):
                neighbors.append((i, j - 1))
            if j < self._cols -1 and (i, j + 1) not in visited and self.is_connected(i, j, Wall.RIGHT):
                neighbors.append((i, j + 1))


            if len(neighbors) == 0:
                p = prev.pop()
                # Put previous back on the worklist to fix drawing
                worklist.append(p)
                self.__draw_path(current, p, True)
            else: 
                worklist.extend(neighbors)
                prev.append(current)
        
        print("-- Solved --")
            

    def is_connected(self, i, j, wall):
        return not self._cells[i][j].has_wall(wall)
    


