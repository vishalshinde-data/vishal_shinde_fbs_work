#Write a program to calculate area of circle.
def circle_area(radius):
    area = 3.14 * radius * radius
    return area
r = 5

res = circle_area(r)
print("Area of circle:", res)