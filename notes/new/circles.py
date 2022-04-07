from graphics import GraphWin, Circle, Point, Text

win = GraphWin('win',400,400)
ne = Text(Point(200,200),'hello')
ne.draw(win)
print(ne.getText())
