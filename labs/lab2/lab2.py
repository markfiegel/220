"""
Mark Fiegel
lab2.py
I made a program that calculates 3 different formulas with inputted data
I certify that this assignment is entirely my own work.
"""
import math
def means():
    range_values = eval(input("How many inputs do you have? "))
    rms_accum = 0
    harm = 0
    geo = 1
    for i in range(range_values):
        x = eval(input("value? "))
        rms_accum = rms_accum + x**2
        harm = harm + 1/x
        geo = geo * x
    rms = (rms_accum/range_values) ** (1/2)
    rms = round(rms,3)
    harmonic_form = (range_values/harm)
    harmonic_form = round(harmonic_form,3)
    geometric_mean = (geo)**(1/range_values)
    geometric_mean = round(geometric_mean,3)
    print("Your root mean square is", rms)
    print("Your harmonic mean is", harmonic_form)
    print("Your geometric mean is", geometric_mean)
    print(harm)
means()