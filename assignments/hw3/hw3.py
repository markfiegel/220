"""
Mark Fiegel
hw3.py
I was given a series of problems that I created simple programs for
I certify that this assignment is entirely my own work.
"""
import math
def average():
    average_accum = 0
    grades = eval(input("how many grades?  "))
    for i in range(0,grades):
        all_grades = eval(input("what's the grade?  "))
        average_accum = average_accum + all_grades
    print("average is" , average_accum/grades)



def tip_jar():
    tip_accum = 0
    for i in range(5):
        tips = eval(input("How much would you like to donate?  "))
        tip_accum = tip_accum + tips
    print("total tips  " , tip_accum)

def newton():
    x_newton = eval(input("x?"))
    approx = eval(input("approximation?"))
    x_val = 1
    for i in range(1,approx+1):
        next_x = (x_val+(x_newton/x_val))*.5
        x_val = next_x
    print(next_x)
def sequence():
    terms = eval(input("how many terms are there?"))
    for i in range (terms +1):
        print(i)
def pi():
    accum = 2
    accum_2 = 1
    approx = eval(input("how many terms in the series?"))
    for i in range(1, approx+1):
        first = (2*i)/((2*i)+1)
        second = (2*i)/((2*i)-1)
        accum = first * second
        accum_pi = accum * accum_2
    print(accum_pi*math.pi)
pi()