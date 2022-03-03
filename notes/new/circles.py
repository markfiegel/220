import graphics
from graphics import GraphWin, Entry, Point, Text

def vigenere():
    win = GraphWin("win", 500,500)
    code_message = Text(Point(100,150),"Message to code")
    keyword_message = Text(Point(100,200), "Enter keyword")
    box_message = Entry(Point(350,150),30)
    box_keyword = Entry(Point(350,200), 20)
    box_keyword.draw(win)
    keyword_message.draw(win)
    box_message.draw(win)
    code_message.draw(win)
    win.getMouse()
    message_text  = box_message.getText()
    keyword_text = box_keyword.getText()
    message_replace= message_text.replace(" ","")
    keyword_replace = keyword_text.replace(" ","")
    message_replace = message_replace.upper()
    keyword_replace = keyword_replace.upper()
    end_char = ""
    len_key = len(keyword_replace)
    for i in range(len(message_replace)):
        my_ord = ord(message_replace[i])
        key_ord = ord(keyword_replace[i%len_key])
        ord_add = ((my_ord-65)+(key_ord-65))%26
        new_char = chr(ord_add+65)
        end_char = end_char+new_char
    result = Text(Point(250,375), "Click to close")
    resulting_message = Text(Point(250,280),"Resulting Message")
    resulting_message.draw(win)
    ending = Text(Point(250,300),end_char)
    ending.draw(win)
    result.draw(win)
    win.getMouse()
    win.close()
vigenere()