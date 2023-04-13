import math


def area_and_capacity_circle(r):
    area = 4 * math.pi * math.pow(r, 2)
    capacity = 4/3 * math.pi * math.pow(r, 3)
    return round(area, 2), round(capacity, 2)


def area_and_capacity_cone(r, h):
    l = math.sqrt(math.pow(r, 2) + math.pow(h, 2))
    area = math.pi * r * (r + l)
    capacity = 1/3 * math.pi * math.pow(r, 2) * h
    return round(area, 2), round(capacity, 2)


def area_and_capacity_cube(a):
    area = 6 * math.pow(a, 2)
    capacity = math.pow(a, 3)
    return round(area, 2), round(capacity, 2)


print(area_and_capacity_circle(3))
print(area_and_capacity_cone(3, 4))
print(area_and_capacity_cube(3))
