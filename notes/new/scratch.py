from button import button
from graphics import Rectangle, Text , Point , GraphWin
win  = GraphWin('win',700,700)
rec = Rectangle(Point(50,50),Point(200,200))
d = Button()
d.shape = rec
d.label = 'hello'