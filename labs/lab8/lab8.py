"""
Mark Fiegel
lab8.py
I just couldnt figure it out
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import Circle, Point, GraphWin, color_rgb
import time

def get_random():
    return randint(-3.0,3.0)
def did_collide(ball, ball_2):
    ball_x = ball.getCenter().getX()
    ball_y = ball.getCenter().getY()
    ball_2_x = ball_2.getCenter().getX()
    ball_2_y = ball_2.getCenter().getY()
    distance = (((ball_2_x-ball_x)**2)+((ball_2_y-ball_y)**2))
    if distance < 40:
        collide = True
    else:
        False
    return distance
def hit_vertical(ball):
    y_val = ball.getCenter().getY()
    if y_val >= 380:
        hit_ver = True
    elif 20 >= y_val:
        hit_ver = True
    else:
        hit_ver = False
    return hit_ver
def hit_horizontal(ball,win):
    x_val = ball.getCenter().getX()
    if x_val >= 380:
        hit_hor = True
    elif 20 >= x_val:
        hit_hor = True
    else:
        hit_hor = False
    return hit_hor
def get_random_color():
    return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
def bumper():
    win = GraphWin("win",400,400)
    circ = Circle(Point(150,200),40)
    circ_2 = Circle(Point(250,200),40)
    circ.setFill(get_random_color())
    circ_2.setFill(get_random_color())
    circ.draw(win)
    circ_2.draw(win)
    circ_1_move = (get_random())
    circ_2_move = (get_random())
    x = 0
    while x <10:
        circ.move(circ_1_move/20,circ_1_move/20)
        circ_2.move(circ_2_move/20,circ_2_move/20)
        if hit_horizontal(circ,win):
            circ.move(((circ_1_move / 20)*-1), circ_1_move / 20)
        if hit_horizontal(circ_2,win):
            circ.move(((circ_2_move / 20)*-1), circ_2_move / 20)
        if hit_vertical(circ,win):
            circ.move((circ_1_move / 20), ((circ_1_move / 20)*-1))
        if hit_vertical(circ_2,win):
            circ_2.move((circ_2_move / 20), ((circ_2_move / 20)*-1))
        if did_collide():
            circ.move(((circ_1_move / 20)*-1), ((circ_1_move / 20)*-1))
            circ_2.move(((circ_2_move / 20)*-1), ((circ_2_move / 20)*-1))

bumper()