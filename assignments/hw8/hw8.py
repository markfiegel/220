"""
Mark Fiegel
hw8.py

I completed a series of functions
I certify that this assignment is entirely my own work.
"""
import math
from graphics import GraphWin, Point, Circle, Text

def add_ten(nums):
    num_len = len(nums)
    for i_val in range(num_len):
        x_val = nums[i_val] +10
        nums.append(x_val)
    del nums[0:num_len]
def square_each(nums):
    num_len = len(nums)
    for i in range(num_len):
        x_val = nums[i]**2
        nums.append(x_val)
    del nums[0:num_len]

def sum_list(nums):
    num_len = len(nums)
    sum_accum = 0
    for i in range(num_len):
        sum_accum = sum_accum + nums[i]
    x_val = sum_accum
    return x_val
def to_numbers(nums):
    num_len = len(nums)
    for i in range(num_len):
        if isinstance(nums[i],int):
            x_val = int(nums[i])
            nums.append(x_val)
        else:
            x_val = float(nums[i])
            nums.append(x_val)
    del nums[0:num_len]
def sum_of_squares(nums):
    sum_of_sq_list = []
    num_len = len(nums)
    for i in range(num_len):
        x_val = str(nums[i])
        new_list = x_val.split(',')
        to_numbers(new_list)
        square_each(new_list)
        new_val= sum_list(new_list)
        sum_of_sq_list.append(new_val)
    return sum_of_sq_list

def starter(weight, wins):
    starter_win = bool(weight>199 or wins> 20) or ((weight>=150 and weight<160) and wins>=5)
    return starter_win

def leap_year(year):
    if (year%4== 0) and (year%100!=0):
        years = True
    elif year%400==0:
        years = True
    else:
        years = False
    return years
def did_overlap(circle_one, circle_two):
    circle_x = circle_one.getCenter().getX()
    circle_y = circle_one.getCenter().getY()
    circle_2_x = circle_two.getCenter().getX()
    circle_2_y = circle_two.getCenter().getY()
    distance = (((circle_2_x - circle_x) ** 2) + ((circle_2_y - circle_y) ** 2))**(1/2)
    radius = circle_one.getRadius()
    radius_2 = circle_two.getRadius()
    overlap = bool(radius+radius_2>= distance)
    return overlap
def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(  (center_2.getX() - circumference_point_2.getX())
                           ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2,radius_2)
    circle_two.draw(win)
    overlap_text = Text(Point(width/2,height/2),"It did overlap")
    non_overlap_text = Text(Point(width/2,height/2), "It did not overlap")
    if did_overlap(circle_one,circle_two):
        overlap_text.draw(win)
    else:
        non_overlap_text.draw(win)
    win.getMouse()
if __name__ == '__main__':
    pass
