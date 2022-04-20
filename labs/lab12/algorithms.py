"""
Mark Fiegel
lab12.py
I did a series of challenges without being able to use a for loop
I certify that this assignment is entirely my own work.
"""
from graphics import Rectangle, Point
def read_data(file_name):
        files = open(file_name,'r')
        new_list = files.read()
        new_list = new_list.replace('\n',' ')
        new_list = new_list.split(' ')
        print(new_list)
def is_in_linear(search_val,values):
    count = 0
    while count< len(values):
        if values[count] == search_val:
            return True
        count = count + 1
    return False

def selection_sort(values):
    for i in range(len(values)):
        min = i
        for j in range(i,len(values)):
            if values[j] < values[min]:
                min = j
        temp = values[i]
        values[i] = values[min]
        values[min] = temp

    return values

def is_in_binary(search_val, values):
    lower = 0
    upper = len(values)-1
    values = selection_sort(values)
    while lower <= upper:
        mid = (lower+upper)//2
        if values[mid] == search_val:
            position = mid
            return True, position
        else:
            if values[mid] < search_val:
                lower = mid+1
            else:
                upper = mid+1
    return False
def rect_sort(rectangles):
    list = []
    for i in range(len(rectangles)):
        x_value = rectangles[i].getP2().getX() - rectangles[i].getP1().getX()
        y_value = rectangles[i].getP2().getY() - rectangles[i].getP1().getY()
        area = x_value * y_value
        list.append(area)
    new_list = selection_sort(list)
    return new_list

rect_sort([Rectangle(Point(10,10),Point(100,80)),Rectangle(Point(100,10),Point(150,200)),Rectangle(Point(200,190),Point(220,200))])