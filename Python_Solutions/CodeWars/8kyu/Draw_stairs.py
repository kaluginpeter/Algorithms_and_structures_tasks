# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
#
# For example n = 3 result in:
#
# "I\n I\n  I"
# or printed:
#
# I
#  I
#   I
# Another example, a 7-step stairs should be drawn like this:
#
# I
#  I
#   I
#    I
#     I
#      I
#       I
# ASCII ARTALGORITHMS
# Solution
def draw_stairs(n):
    output_string = ''
    for num in range(0,n-1):
        output_string += ' '*num + 'I\n'
    output_string +=  ' '*(n-1) + 'I'
    return output_string