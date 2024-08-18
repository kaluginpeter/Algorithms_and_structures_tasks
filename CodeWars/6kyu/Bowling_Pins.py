# Mount the Bowling Pins!
# Task:
# Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:
#
#
# I I I I  # each Pin has a Number:    7 8 9 10
#  I I I                                4 5 6
#   I I                                  2 3
#    I                                    1
#
# You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:
#
#
# I I   I
#  I   I
#   I
#    I
#
# Return a string with the current field.
#
# Note that:
# You begin a new line with \n
# Each Line must be 7 chars long
# Fill the missing pins with a whitespace
# Have fun!
# ARRAYSSTRINGSFUNDAMENTALS
# Solution
def bowling_pins(arr):
    pins, word = '   1   \n  2 3  \n 4 5 6 \n7 8 9 I', ''
    for i in arr:
        if i == 10:
            pins = pins[:-1] + ' '
            continue
        pins = pins.replace(str(i), ' ')
    for i in pins.split('\n')[::-1]:
        print(i)
        for j in i:
            word += ' ' if j == ' ' else 'I'
        word += '\n'
    return word[:-1]