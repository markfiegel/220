"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math

def cash_converter():
    cash = input("enter an integer:  ")
    cash = float(cash)
    format_cash = "{:.2f}".format(cash)
    txt_1 = "that is ${}".format(format_cash)
    print(txt_1)

def encode():
    message = input("enter a message ")
    key = eval(input("enter a key"))
    len_message = len(message)
    listy = ''
    for i_val in range(len_message):
        x_val = ord(message[i_val])
        x_val = int(x_val)
        y_val = chr(x_val+key)
        x_str= ''+y_val
        listy = listy+x_str
    print(listy)
encode()

def sphere_area(radius):
    return 4*(math.pi)*(radius**2)
def sphere_volume(radius):
    return (4/3)*(math.pi)*(radius**3)
def sum_n(number):
    x_val = 0
    for i_val in range(1,number+1):
        x_val = x_val+i_val
    return x_val

def sum_n_cubes(number):
    x_val = 0
    for i_val in range(1,number+1):
        i_val = i_val**3
        x_val = x_val+i_val
    return x_val

def encode_better():
    pass
