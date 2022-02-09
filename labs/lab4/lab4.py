"""
Mark Fiegel
lab4.py
I made a greeting card with motion
I certify that this assignment is entirely my own work.
"""

import graphics
import time
from graphics import Polygon, GraphWin, Point, Circle, Line , Text

def greeting_card():
    win = GraphWin("Greeting Card", 400,400)
    heart_poly = Polygon(Point(200,300),Point(289,110),Point(111,110),Point(200,300))
    circ_1 = Circle(Point(160,100),50)
    circ_2 = Circle(Point(240,100),50)
    heart_poly.setFill('red')
    heart_poly.setOutline('red')
    circ_2.setOutline('red')
    circ_1.setOutline('red')
    circ_1.setFill('red')
    circ_2.setFill('red')
    heart_poly.draw(win)
    circ_1.draw(win)
    circ_2.draw(win)
    arrow = Line(Point(388,390),Point(500,515))
    arrow.setOutline('brown')
    arrow_head = Polygon(Point(385,385),Point(400,390),Point(385,400))
    arrow_head.setFill('black')
    arrow.draw(win)
    arrow_head.draw(win)
    happy = Text(Point(200,10), "Happy Valentines!!")
    happy.draw(win)
    time.sleep(1)
    i = 1000
    for i in range(i):
        arrow.move(-.2,-.2)
        arrow_head.move(-.2,-.2)
    time.sleep(1.5)
    ending = Text(Point(200,370), "Click to close")
    ending.draw(win)
    win.getMouse()
    win.close()
greeting_card()