"""
Mark Fiegel
hw10.py
i did a series of challenges without using a for loop
I certify that this assignment is entirely my own work.
"""
from graphics import Circle, Line, Polygon, Point
class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.size = size
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)
    def smile(self):
        pointer = self.mouth.getP1()
        pointer_2 = self.mouth.getP2()
        lower = (pointer_2.getX() + pointer.getX())/2
        self.mouth.undraw()
        self.smiles = Polygon(pointer,pointer_2,Point(lower,pointer.getY()+20))
        self.smiles.draw(self.window)
        self.window.getMouse()
        self.window.close()

    def shock(self):
        pointer = self.mouth.getP1()
        pointer_2 = self.mouth.getP2()
        lower = (pointer_2.getX() + pointer.getX()) / 2
        self.mouth.undraw()
        self.shock_mouth = Circle(Point(lower,pointer.getY()),self.size*.15)
        self.shock_mouth.draw((self.window))
        self.window.getMouse()
        self.window.close()

    def wink(self):
        pointer = self.mouth.getP1()
        pointer_2 = self.mouth.getP2()
        lower = (pointer_2.getX() + pointer.getX()) / 2
        new_x = self.left_eye.getCenter()
        new_x_rad = self.left_eye.getRadius()
        new_eye = Line(Point(new_x.getX()-new_x_rad,new_x.getY()),Point(new_x.getX()+new_x_rad,new_x.getY()))
        self.left_eye.undraw()
        new_eye.draw(self.window)
        self.mouth.undraw()
        self.smiles = Polygon(pointer, pointer_2, Point(lower, pointer.getY() + 20))
        self.smiles.draw(self.window)
        self.window.getMouse()
        self.window.close()

