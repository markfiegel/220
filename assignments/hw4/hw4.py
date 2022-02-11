"""
Mark Fiegel
hw4.py
I did a series of challenges with the graphics library
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin, Text, Point, Rectangle, Circle

def squares():
    win = GraphWin("Window", 400, 400)
    rect = Rectangle(Point(100, 100), Point(150, 150))
    starter = Text(Point(200, 20), "Click to draw")
    starter.draw(win)
    rect.draw(win)
    for _ in range(5):
        x_val = win.getMouse()
        center = rect.getCenter()
        new_x = x_val.getX() - center.getX()
        new_y = x_val.getY() - center.getY()
        new_rect = rect.clone()
        new_rect.move(new_x, new_y)
        new_rect.draw(win)
    closer = Text(Point(200, 305), "Click to Close")
    closer.draw(win)
    win.getMouse()
def rectangle():
    win = GraphWin("Window",400,400)
    x_val = win.getMouse()
    y_val = win.getMouse()
    rect = Rectangle(x_val,y_val)
    rect.draw(win)
    height = abs(abs(x_val.getY())-abs(y_val.getY()))
    width = abs(abs(x_val.getX())-abs(y_val.getX()))
    area = height*width
    perimeter = 2*(height+width)
    area_text = Text(Point(200,380),"Your area is:")
    new_area_txt = Text(Point(290,380), area)
    perim_text = Text(Point(200,350),"Your Perimeter is:")
    new_perim_text = Text(Point(290,350), perimeter)
    new_perim_text.draw(win)
    perim_text.draw(win)
    area_text.draw(win)
    new_area_txt.draw(win)
    closer = Text(Point(200,20),"Click to close")
    closer.draw(win)
    win.getMouse()
def circle():
    win = GraphWin("Window", 300, 300)
    x_val = win.getMouse()
    y_val = win.getMouse()
    x_1 = x_val.getX()
    x_2 = y_val.getX()
    y_1 = x_val.getY()
    y_2 = y_val.getY()
    final_x = (x_2 - x_1) ** 2
    final_y = (y_2 - y_1) ** 2
    dist = math.sqrt(final_x + final_y)
    circ = Circle(x_val, dist)
    circ.draw(win)
    radius = Text(Point(70, 280), "Radius:")
    radii = Text(Point(175, 280), dist)
    radius.draw(win)
    radii.draw(win)
    closer = Text(Point(150, 20), "Click to close")
    closer.draw(win)
    win.getMouse()
def pi2():
    terms = eval(input("How many terms? "))
    approx_accum = 0
    denom = 1
    additive = 2
    for _ in range(terms):
        approx = 4 / denom
        denom = (denom + additive)
        approx_accum = approx_accum + approx
        denom = denom * -1
        additive = additive * -1
    print("Pi approximation: ", approx_accum)
    print("Accuracy: ", abs(math.pi - approx_accum))
