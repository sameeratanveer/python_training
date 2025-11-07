'''
Calculate area and circumference of a circle (use math.pi).
pi r*2
2 pi r
'''
from math import pi
r = float(input("Enter the radius of the circle: "))
print(f"Area of the circle : {pi*r*r}")
print(f"Circumference of the circle: {2*pi*r}")
