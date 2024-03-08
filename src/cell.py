from enum import Enum
from shapes import Point, Line
from tkinter import Canvas

from window import Window

class Wall(Enum):
    TOP = 0 
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    def opposite(self):
        if self == Wall.TOP:
            return Wall.BOTTOM
        if self == Wall.BOTTOM:
            return Wall.TOP
        if self == Wall.LEFT:
            return Wall.RIGHT
        if self == Wall.RIGHT:
            return Wall.LEFT

class Cell:
    def __init__(self, location: Point, window: Window, scale = 25):
        self.__walls = [True, True, True, True]
        self.__location = location
        self.__window = window
        self.__rescale__(scale)

    def __repr__(self) -> str:
        return f"Cell({self.__ul},{self.__lr})"


    def __rescale__(self,scale):
        self.__ul = Point(
            self.__location.x * scale, 
            self.__location.y * scale
        )
        self.__lr = Point(
            (self.__location.x * scale) + scale, 
            (self.__location.y * scale) + scale
        )

    def draw(self):
        ul = self.__ul
        lr = self.__lr

        if self.__walls[Wall.TOP.value]:
            line = Line(Point(ul.x, ul.y), Point(lr.x, ul.y))
            self.__window.draw_line(line, "black")

        if self.__walls[Wall.RIGHT.value]:
            line = Line(Point(lr.x, ul.y), Point(lr.x, lr.y))
            self.__window.draw_line(line, "black")

        if self.__walls[Wall.BOTTOM.value]:
            line = Line( Point(ul.x, lr.y), Point(lr.x, lr.y))
            self.__window.draw_line(line, "black")

        if self.__walls[Wall.LEFT.value]:
            line = Line( Point(ul.x, ul.y), Point(ul.x, lr.y))
            self.__window.draw_line(line, "black")

    def draw_move(self, other, undo = False): 
        color = "red"
        if undo:
            color = "gray"

        line = Line(self.scaled_center(), other.scaled_center())
        self.__window.draw_line(line, color)

    def scaled_center(self):
        
        return Point((self.__ul.x + self.__lr.x // 2), 
                     (self.__ul.y + self.__lr.y // 2))


    def has_top(self, w=True):
        self.has_wall(Wall.TOP, w)

    def has_left(self, w=True):
        self.has_wall(Wall.LEFT, w)
    
    def has_right(self, w=True):
        self.has_wall(Wall.RIGHT, w)
   
    def has_bottom(self, w=True):
        self.has_wall(Wall.BOTTOM, w)

    def has_wall(self, wall: Wall, w: bool):
        self.__walls[wall.value] = w
