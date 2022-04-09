"""
Mark Fiegel
hw10.py
i did a series of challenges without using a for loop
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Point
from face import Face

def fibonacci(number):
    a_val= 0
    b_val = 1
    summ = 0
    counter = 1
    while counter <= number:
        counter += 1
        a_val = b_val
        b_val = summ
        summ = a_val + b_val
    return summ
def double_investment(principle, rate):
    ann = principle
    counter = 0
    while ann <= 2*principle:
        ann = ann *(1+rate)
        counter += 1
    return counter
def syracuse(num):
    syracuse_list = [num]
    while num !=1:
        if num%2 ==0:
            num = num/2
            syracuse_list.append(num)
        else:
            num = 3 * num +1
            syracuse_list.append(num)
    return syracuse_list
def goldbach(number):
    pass
f = Face(GraphWin('win',500,500),Point(250,250),100)
f.wink()
