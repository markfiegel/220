"""
Mark Fiegel
lab5.py
I solved a series of problems using the graphics library and strings
I certify that this assignment is entirely my own work.
"""
import math
import graphics
from graphics import GraphWin, Polygon, Text, Point, Circle, Entry, color_rgb
def triangle():
    win = GraphWin("window", 400,400)
    x_1 = win.getMouse()
    x_val1 = x_1.getX()
    y_val1 = x_1.getY()
    x_2 = win.getMouse()
    x_val2 = x_2.getX()
    y_val2 = x_2.getY()
    x_3 = win.getMouse()
    x_val3 = x_3.getX()
    y_val3 = x_3.getY()
    poly = Polygon(x_1,x_2,x_3)
    poly.draw(win)
    dx_1 = x_val2 - x_val1
    dy_1 = y_val2 - y_val1
    dx_2 = x_val3 - x_val2
    dy_2 = y_val3 - y_val2
    dx_3 = x_val1 - x_val3
    dy_3 = y_val1 - y_val3
    length_1 = ((dx_1**2)+(dy_1**2))**(1/2)
    length_2 = ((dx_2**2)+(dy_2**2))**(1/2)
    length_3 = ((dx_3 ** 2) + (dy_3 ** 2)) ** (1 / 2)
    perim = length_3+length_2+length_1
    s_val = perim/2
    area = (s_val*(s_val - length_1)*(s_val- length_2)*(s_val-length_3))**(1/2)
    area_display = Text(Point(100,325),"Your area is:")
    area_show = Text(Point(250,325), area)
    area_display.draw(win)
    area_show.draw(win)
    perimeter = Text(Point(100,350),"Your perimeter is:")
    new_perim = Text(Point(250,350), perim)
    new_perim.draw(win)
    perimeter.draw(win)
    closer = Text(Point(200,10),"Click to close")
    closer.draw(win)
    win.getMouse()
    win.close()
def color_shape():
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(200,240),5)
    red_entry.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(Point(200,268),5)
    green_entry.draw(win)
    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(Point(200,296),5)
    blue_entry.draw(win)
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    for _ in range(5):
        win.getMouse()
        blue_val = blue_entry.getText()
        blue_val = eval(blue_val)
        green_val = green_entry.getText()
        green_val = eval(green_val)
        red_val = red_entry.getText()
        red_val = eval(red_val)
        circl1 = shape.clone()
        circl1.setFill(color_rgb(red_val,green_val,blue_val))
        circl1.draw(win)
    closer = Text(Point(200, 10), "Click to close")
    closer.draw(win)
    win.getMouse()
    win.close()
def process_string():
    string = input("say anything")
    print(string[0])
    print(string[-1])
    print(string[1:5])
    print(string[0]+string[-1])
    print(string[0:3]*10)
    for i in range(0, len(string)):
        print(string[0+i])
    print(len(string))
def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = (values[1]+values[3])
    print(x)
    val = float(values[0])
    val_2 = float(values[2])
    x = val + val_2
    print(x)
    x = values[1]*5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4]
    x.append(values[0])
    print(x)
    val = float(values[5])
    x = values
    x.append(val)
    x = (x[2],x[0],x[6])
    print(x)
    x = values[0]+values[2]+val
    print(x)
    x = values[0:6]
    print(len(x))

def another_series():
    nums = eval(input("number of terms:"))
    nums = nums*5
    for i in range(1,nums+1,2):
        i = i
        x = i%5
        print(x)

def target():
    win = GraphWin("win",400,400)
    radius = 200
    radius2 = radius/5
    yellow_circ = Circle(Point(200,200),radius/5)
    yellow_circ.setOutline("yellow")
    white_circ = Circle(Point(200,200), radius)
    white_circ.setOutline("white")
    red_circ = Circle(Point(200,200),radius2*2 )
    red_circ.setOutline("red")
    blue_circ = Circle(Point(200,200),radius2*3)
    blue_circ.setOutline("blue")
    black_circ = Circle(Point(200,200),radius2*4)
    black_circ.setOutline("black")

    white_circ.draw(win)
    black_circ.draw(win)
    blue_circ.draw(win)
    red_circ.draw(win)
    yellow_circ.draw(win)
    closer = Text(Point(200, 10), "Click to close")
    closer.draw(win)
    win.getMouse()
    win.close()
