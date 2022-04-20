"""
Mark Fiegel
lab13.py
I certify that this assignment is entirely my own work.
"""
from lab12.algorithms import is_in_linear,is_in_binary,selection_sort, rect_sort

def star_find(file_name):
    f = open(file_name,'r')
    x = f.read().split()
    f.close()
    counter = 0
    final_string = ''
    for i in range(len(x)):

        if int(x[i]) >= 4000 and int(x[i]) <= 5000:
            final_string += x[i]
            final_string += ', '
            counter +=1
            if counter == 5:
                fifth = x[i]
    if counter >= 5:
        print(f'It is a neutron star! We found {counter} pulses. The values are {final_string}and the fifth was found at {fifth}'.format(counter = counter, final_string= final_string, fifth= fifth))
    else:
        print("Unfortunately it is not a neutron star")
star_find('signals.txt')


