"""
Mark Fiegel
hw2.py
For this assignment we were given sever functions to program
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    upper_bound_accum = 0
    for i in range(0,upper_bound+1,3):
        upper_bound_accum = upper_bound_accum + i
    print("Your sum of threes is", upper_bound_accum)

def multiplication_table():
    for i_val in range(1,11):
        for x_val in range(1,11):
            num = i_val*x_val
            print(num,end="\t")
        print()
def triangle_area():
    a_val = eval(input("what is a? "))
    b_val = eval(input("what is b? "))
    c_val = eval(input("what is c? "))
    s_val = (a_val+b_val+c_val)/2
    d_val = s_val*(s_val-a_val)*(s_val-b_val)*(s_val-c_val)
    area = math.sqrt(d_val)
    print("your area is", area)
def sum_squares():
    lower= eval(input("lower? "))
    higher= eval(input("higher? "))
    sum_accum = 0
    for i in range (lower, higher+1):
        x_accum= i*i
        sum_accum = sum_accum+x_accum
    print(sum_accum)
def power():
    base = eval(input("base? "))
    exponent = eval(input("exponent?"))
    accum = 1
    for i in range(exponent):
        accum = accum * base
    print(base, " ^ " , exponent, " = ", accum)
