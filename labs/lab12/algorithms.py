"""
Mark Fiegel
lab12.py
I did a series of challenges without being able to use a for loop
I certify that this assignment is entirely my own work.
"""
def read_data(file_name):
        files = open(file_name,'r')
        new_list = files.read()
        new_list = new_list.replace('\n',' ')
        new_list = new_list.split(' ')
        print(new_list)
def is_in_linear(search_val,values):
    if values.count(search_val)>= 1:
        return True
    else:
        return False