"""
from graphics import GraphWin, Rectangle, Text, Point
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
    def get_label(self):
        new_lab = str(self.label())
        return new_lab
    def set_label(self):
        label_d = Text(Point(200,75),self.get_label())
        return label_d
    def draw(self,win):
        self.shape.draw(win)
        self.set_label().draw(win)
    def undraw(self):
        self.shape.undraw()
        self.set_label().undraw()
    def is_clicked(self,point):
        x_val = point.getX()
        y_val = point.getY()
        if (x_val<=300 and x_val>=100) and (y_val <=100 and y_val>=50):
            clicked = True
        else:
            clicked = False
        return clicked
    def color_button(self,color):
        self.shape.setFill(color)