# Write a function that returns the total surface area and volume of a box as an array: [area, volume]
#
# GEOMETRYFUNDAMENTALS
# Solution
def get_size(w,h,d):
    return [((w * h) + (w * d) + (h * d)) * 2, w * h * d]