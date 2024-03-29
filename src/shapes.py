from tkinter import Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

    def draw(self, canvas: Canvas, color: str):
        canvas.create_line(self.x, self.y, self.x, self.y, fill=color, width=3)

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, color: str):
        canvas.create_line(
                self.start.x, 
                self.start.y, 
                self.end.x, 
                self.end.y, 
                fill=color, width=2)
