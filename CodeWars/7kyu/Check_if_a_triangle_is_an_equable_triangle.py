# A triangle is called an equable triangle if its area equals its perimeter. Return true, if it is an equable triangle, else return false. You will be provided with the length of sides of the triangle. Happy Coding!
#
# FUNDAMENTALSGEOMETRY
# Solution
def equable_triangle(a,b,c):
    p = (a + b + c) / 2
    return (p*(p-a)*(p-b)*(p-c)) ** .5 == a + b + c