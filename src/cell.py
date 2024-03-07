from enum import Enum
from shapes import Point, Line
from tkinter import Canvas

from window import Window

class Wall(Enum):
    TOP = 0 
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

class Cell:
    def __init__(self, location: Point, window: Window):
        self.__walls = [True, True, True, True]
        self.__location = location
        self.__window = window

    def draw(self, scale = 25):
        if self.__walls[Wall.TOP.value]:
            line = Line(
                    Point(self.__location.x, self.__location.y), 
                    Point(self.__location.x + scale, self.__location.y))
            self.__window.draw_line(line, "black")
        if self.__walls[Wall.RIGHT.value]:
            line = Line(
                    Point(self.__location.x + scale, self.__location.y), 
                    Point(self.__location.x + scale, self.__location.y + scale))
            self.__window.draw_line(line, "black")
        if self.__walls[Wall.BOTTOM.value]:
            line = Line(
                    Point(self.__location.x + scale, self.__location.y + scale), 
                    Point(self.__location.x, self.__location.y + scale))
            self.__window.draw_line(line, "black")
        if self.__walls[Wall.LEFT.value]:
            line = Line(
                    Point(self.__location.x, self.__location.y), 
                    Point(self.__location.x, self.__location.y + scale))
            self.__window.draw_line(line, "black")

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
