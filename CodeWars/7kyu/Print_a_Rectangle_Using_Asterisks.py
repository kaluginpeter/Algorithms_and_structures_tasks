# Write a method that, given two arguments, width and height, returns a string representing a rectangle with those dimensions.
#
# The rectangle should be filled with spaces, and its borders should be composed of asterisks (*).
#
# For example, given width = 3 and height = 3:
#
# ***
# * *
# ***
# End each line of the string (including the last one) with a carriage return-line feed combination.
#
# Note: You may assume that width and height will always be greater than zero.
#
# StringsASCII ArtAlgorithms
# Solution
def get_rectangle_string(width, height):
    output: list[str] = []
    for i in range(height):
        if not i or i + 1 == height:
            output.append('*' * width + '\r\n')
        else:
            output.append('*' + ' ' * (width - 2) + '*\r\n')
    return ''.join(output)