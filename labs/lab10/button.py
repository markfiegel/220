"""
Mark Fiegel
lab10.py
I made several classes then integrated them into a function
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Rectangle, Text, Point
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
    def get_label(self):
        new_lab = self.label
        return new_lab
    def set_label(self):
        x_val = self.shape.getP1()
        x_val_2 = self.shape.getP2()
        new_y = x_val.getY() + ((x_val_2.getY() - x_val.getY())/2)
        new_x = x_val.getX() + ((x_val_2.getX() - x_val.getX())/2)
        label_d = Text(Point(new_x,new_y),self.get_label())
        return label_d
    def draw(self,win):
        self.shape.draw(win)
        self.color_button()
        self.set_label().draw(win)
    def undraw(self,win):
        self.shape.undraw(win)
        self.set_label().undraw(win)
    def is_clicked(self,point):
        x_val = point.getX()
        y_val = point.getY()
        x_p1 = self.shape.getP1()
        x_p2 = self.shape.getP2()
        if (x_val <= x_p2.getX() and x_val >= x_p1.getX()) and (y_val >= x_p1.getY() and y_val <= x_p2.getY()):
            clicked = True
        else:
            clicked = False
        return clicked
    def color_button(self):
        self.shape.setFill('light blue')