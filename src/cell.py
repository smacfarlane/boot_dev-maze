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
    def __init__(self, location: Point, window: Window, scale = 25):
        self.__walls = [True, True, True, True]
        self.__location = location
        self.__window = window
        self.__scale = scale

    def draw(self):
        scale = self.__scale
        offset_x = self.__location.x * self.__scale
        offset_y = self.__location.y * self.__scale

        if self.__walls[Wall.TOP.value]:
            line = Line(
                    Point(offset_x, offset_y), 
                    Point(offset_x + scale, offset_y))
            self.__window.draw_line(line, "black")
        if self.__walls[Wall.RIGHT.value]:
            line = Line(
                    Point(offset_x + scale, offset_y), 
                    Point(offset_x + scale, offset_y + scale))
            self.__window.draw_line(line, "black")
        if self.__walls[Wall.BOTTOM.value]:
            line = Line(
                    Point(offset_x + scale, offset_y + scale), 
                    Point(offset_x, offset_y + scale))
            self.__window.draw_line(line, "black")
        if self.__walls[Wall.LEFT.value]:
            line = Line(
                    Point(offset_x, offset_y), 
                    Point(offset_x, offset_y + scale))
            self.__window.draw_line(line, "black")

    def draw_move(self, other, undo = False): 
        color = "red"
        if undo:
            color = "gray"

        line = Line(self.scaled_center(), other.scaled_center())
        self.__window.draw_line(line, color)

    def scaled_center(self):
        offset_x = self.__location.x * self.__scale
        offset_y = self.__location.y * self.__scale
        
        return Point(offset_x + self.__scale // 2, 
                     offset_y + self.__scale // 2)


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
