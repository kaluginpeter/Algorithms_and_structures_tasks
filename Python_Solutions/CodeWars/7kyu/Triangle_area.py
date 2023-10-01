# Task.
#
# Calculate area of given triangle. Create a function t_area that will take a string which will represent triangle, find area of the triangle, one space will be equal to one length unit. The smallest triangle will have one length unit.
#
# Hints
#
# Ignore dots.
#
# All triangles will be right isoceles.
#
# Example:
#
# .
# .      .
# .      .       .      ---> should return 2.0
#
# .
# .      .
# .      .       .
# .      .       .      .      ---> should return 4.5
#
# MATHEMATICSFUNDAMENTALS
# Solution
def t_area(s):
    return (s.count('\n') - 2) ** 2 / 2