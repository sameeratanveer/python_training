'''
Convert user-entered angle degrees → radians → sin, cos, tan.
'''

import math
angle = float(input("Enter angle: "))
print(f"Angle {angle} -> radians {math.radians(angle):.2f}")
print(f"sin({angle}) = {math.sin(angle):.2f}")
print(f"cos({angle}) = {math.cos(angle):.2f}")
print(f"tan({angle}) = {math.tan(angle):.2f}")


