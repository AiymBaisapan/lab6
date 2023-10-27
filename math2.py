def trapezoid_area(a, b, h):
    area = 0.5 * (a + b) * h
    return area
h = float(input("height: "))
a = float(input("base, first value: "))
b = float(input("base, second value: "))

area = trapezoid_area(a, b, h)
print("The area of the trapezoid is:", area)
