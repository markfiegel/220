"""
Mark Fiegel
hw5.py

I was given a series of challenges with strings
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def name_reverse():
    namer = input("what is your first and last name? ")
    name = namer.split(" ")
    name.append(",")
    print(name[1]+name[2], name[0])
def company_name():
    domain = input("what is the domain")
    domain = domain.split(".")
    print(domain[1])

def initials():
    students = eval(input("how many students in the class? "))
    for _ in range(1,students+1):
        mylist = input("what is the name? ")
        mylist = mylist.split()
        final =mylist[0][0]+mylist[1][0]
        print(final)
def names():
    namer = input("what are the names? ")
    namer.upper()
    names = namer.split(" ")

    names_count = len(names)
    for i in range(0,names_count-1,2):
        namess = names[i][0]+names[i+1][0]
        namess.title()
        print(namess, end=" ")
def thirds():
    sentence_num = eval(input("how many sentences?"))
    x_val = []
    for i in range(1, sentence_num+1):

        print("enter sentence", i)
        y_val = input("")
        x_val.append(y_val[0::3])
    for j in range(sentence_num):
        print(x_val[j])
thirds()
def word_average():
    sentence = input("enter a sentence: ")
    sentences = sentence.split()
    sentence_len = len(sentences)
    x_val = 0
    for i in range(sentence_len):
        y_val = len(sentences[i])
        x_val = x_val+y_val
    print(x_val/sentence_len)
def pig_latin():
    words = input("enter a sentence to convert to pig latin: ").split()
    for word in words:
        wordes = word[1:] + word[0]
        print(wordes.lower() + "ay", end=" ")