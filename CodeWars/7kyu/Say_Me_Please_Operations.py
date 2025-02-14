# You have a string of numbers; starting with the third number each number is the result of an operation performed using the previous two numbers.
#
# Complete the function which returns a string of the operations in order and separated by a comma and a space, e.g. "subtraction, subtraction, addition"
#
# The available operations are (in this order of preference):
#
# 1) addition
# 2) subtraction
# 3) multiplication
# 4) division
# Notes:
#
# All input data is valid
# The number of numbers in the input string >= 3
# For a case like "2 2 4" - when multiple variants are possible - choose the first possible operation from the list (in this case "addition")
# Integer division should be used
# Example
# "9 4 5 20 25"  -->  "subtraction, multiplication, addition"
# Because:
#
# 9 - 4 = 5   --> subtraction
# 4 * 5 = 20  --> multiplication
# 5 + 20 = 25 --> addition
# AlgorithmsLogicStringsLists
# Solution
def say_me_operations(string_numbers):
    operations: list[str] = []
    words: list[str] = string_numbers.split()
    for i in range(len(words) - 2):
        x: int = int(words[i])
        y: int = int(words[i + 1])
        z: int = int(words[i + 2])
        if x + y == z: operations.append('addition')
        elif x - y == z: operations.append('subtraction')
        elif x * y == z: operations.append('multiplication')
        else: operations.append('division')
    return ', '.join(operations)