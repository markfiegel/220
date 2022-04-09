"""
Mark Fiegel
hw10.py
i did a series of challenges without using a for loop
I certify that this assignment is entirely my own work.
"""
import math
class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def get_radius(self):
        radius = self.radius
        return radius
    def surface_area(self):
        surface_area = 4*math.pi*self.get_radius()**2
        return surface_area
    def volume(self):
        volume = (4/3)* math.pi*self.get_radius()**3
        return volume