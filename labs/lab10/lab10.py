"""
Mark Fiegel
lab10.py
I made several classes then integrated them into a function
I certify that this assignment is entirely my own work.
"""
from button import Button
from door import Door
from graphics import GraphWin, Point, Rectangle, Point, Text
def main():
    win = GraphWin('win',400,400)
    button = Button(Rectangle(Point(100,50),Point(300,100)), 'exit')
    door = Door(Rectangle(Point(100,175),Point(300,400)),'closed')
    button.draw(win)
    door.draw(win)
    door.close(win)
    while button.is_clicked(win.getMouse()) == False:
        if door.is_clicked(win.getMouse()):
            door.is_secret() == False
            if door.is_secret() == True:
                door.undraw()
                door.open(win)
                door.draw(win)
            if door.is_clicked(win.getMouse()):
                door.is_secret() == False
                door.undraw()
                door.close(win)
                door.draw(win)
main()

