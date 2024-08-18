# Given some points (cartesian coordinates), return true if all of them lie on a line. Treat both an empty set and a single point as a line.
#
# on_line(((1,2), (7,4), (22,9)) == True
# on_line(((1,2), (-3,-14), (22,9))) == False
# ARRAYSGEOMETRYFUNDAMENTALS
# Solution
def on_line(p1):
    if len(p1) < 3:
        return True
    step = None
    for i in range(1, len(p1)):
        x: int = p1[i-1][0] - p1[i][0]
        y: int = p1[i-1][1] - p1[i][1]
        if y == 0:
            top: int = 0
        else:
            top: int = x / y
        if not step:
            step = top
        else:
            if top != step:
                return False
    return True