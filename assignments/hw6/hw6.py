"""
Mark Fiegel
hw6.py

This was a series of challenges with encrypting and formatting
Certification of Authenticity:
I certify that this assignment is entirely my own work.
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
    message = input("enter a message: ")
    key = input("enter a key: ")
    message_range = len(message)
    key_range = len(key)
    str_accum = ""
    for i in range(message_range):
        mess_encode = ord(message[i])
        key_encode = ord(key[i%key_range])
        ord_add = ((mess_encode-65)+(key_encode-65))%58
        new_encrypt = chr(ord_add+65)
        str_accum = str_accum + new_encrypt
    print(str_accum)
