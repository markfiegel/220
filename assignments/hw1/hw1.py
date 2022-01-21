"""
Mark Fiegel
hw1.py
For homework 1 it was just a series of sample programming problems
I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

calc_rec_area()

def calc_volume():
    v_length = eval(input("Enter the length: "))
    v_width = eval(input("Enter the width: "))
    v_height = eval(input("Enter the height: "))
    v_area = v_length * v_width * v_height
    print("Area =", v_area)

calc_volume()

def shooting_percentage():
    shots = eval(input("How many shots did you take?"))
    made = eval(input("how many shots did you make?"))
    shooting_percentage= (made/shots)*100
    print(shooting_percentage, "%")

shooting_percentage()

def coffee():
    pounds = eval(input("How many pounds do you want?"))
    coffee = pounds * 10.50
    shipping = pounds * .86
    cost = coffee + shipping + 1.5
    print ("Your total is $",cost)

coffee()

def kilometers_to_miles():
    kilos= eval(input("How many kilometers did you travel   "))
    miles = kilos * .62137119224
    miles = round(miles, 2)
    print("You traveled",miles,"miles!!")

kilometers_to_miles()
