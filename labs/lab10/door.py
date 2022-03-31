from graphics import GraphWin, Rectangle, Text, Point
class Door:
    def __init__(self,shape,label):
        self.shape = shape
        self.label = label
        self.secret = False
    def get_label(self):
        new_lab = self.label
        return new_lab
    def set_label(self):
        label_door = Text(Point(200,300),self.get_label())
        return label_door
    def draw(self,win):
        self.shape.draw(win)
        self.set_label().draw(win)
    def undraw(self):
        self.shape.undraw()
        self.set_label().undraw()
    def is_clicked(self,point):
        x_val = point.getX()
        y_val = point.getY()
        if (x_val <= 300 and x_val >= 100) and (y_val >= 100 and y_val <= 400):
            clicked = True
        else:
            clicked = False
        return clicked
    def open(self,win):
        self.label = 'open'
        self.color_door('white')
    def close(self,win):
        self.color_door('brown')
        self.label = 'closed'
    def color_door(self, color):
        self.shape.setFill(color)
    def is_secret(self):
        if self.set_secret() == True:
            is_a_secret = False
        else:
            is_a_secret = True
        return is_a_secret
    def set_secret(self):
        secrets = self.secret
        return secrets