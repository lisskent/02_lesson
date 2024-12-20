import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = 12.1
area = square(side_length)

print(f"Площадь квадрата со стороной {side_length}: {area}")
