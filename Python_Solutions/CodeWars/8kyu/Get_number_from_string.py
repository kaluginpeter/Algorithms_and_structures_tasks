# Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
#
# Function:
#
# getNumberFromString(s)
# STRINGSREGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def get_number_from_string(string):
    return int(''.join(list(i for i in string if i in '0123456789')))