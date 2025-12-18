import math

def rectangle(x, y):
    return x * y

def square(x):
    return x * x

def circle(r):
    return math.pi * r * r

area_dispatch = {
    "rectangle": lambda x, y: rectangle(x, y),
    "square": lambda x, y: square(x),
    "circle": lambda x, y: circle(x)
}

def calculate_area(shape, x, y=0):
    if shape not in area_dispatch:
        raise ValueError("Invalid shape")
    return area_dispatch[shape](x, y)
