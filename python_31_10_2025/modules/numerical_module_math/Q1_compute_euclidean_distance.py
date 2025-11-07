'''
Compute the Euclidean distance between two user-input points using math.dist().
'''
import math
point1x = float(input("Enter the point1 x : "))
point1y = float(input("Enter the point1 y : "))
point2x = float(input("Enter the point2 x : "))
point2y = float(input("Enter the point2 y : "))
print(f"Euclidean distance between {point1x:.2f}, {point1y:.2f} and {point2x:.2f}, {point2y:.2f}  = {math.dist((point1x, point1y),(point2x,point2y))}")