"""
Mark Fiegel
lab3.py
I made a program that calculates average roads given multiply days and roads
I certify that this assignment is entirely my own work.
"""
def traffic():
    num_roads = eval(input("how many roads are there?  "))
    total = 0
    for i in range(1,num_roads+1):
        print("how many days for road", i,"?", end="\t")
        num_days = eval(input(""))
        road_x = 0
        car_accum= 0
        for y in range(1,num_days+1):
            print("\t", "how many cars on day", y,"?", end = "\t")
            num_cars = eval (input(""))
            car_accum = car_accum +num_cars
            total = total + num_cars
        print("your average cars are", round(car_accum/num_days,3), "for road", i )
    print("Over all roads the total cars are: ", total)
    print("Over all roads the average is:", round(total/num_roads,3))
traffic()
