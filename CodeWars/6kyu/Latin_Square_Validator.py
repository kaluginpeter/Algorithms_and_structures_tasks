# Background
# A latin square is an n × n array filled with the integers 1 to n, each occurring once in each row and column.
#
# Here are examples of latin squares of size 4 and 7:
#
# [ [1, 4, 3, 2],     [ [2, 3, 1, 7, 4, 6, 5],
#   [4, 3, 2, 1],       [7, 1, 6, 5, 2, 4, 3],
#   [3, 2, 1, 4],       [6, 7, 5, 4, 1, 3, 2],
#   [2, 1, 4, 3] ]      [4, 5, 3, 2, 6, 1, 7],
#                       [5, 6, 4, 3, 7, 2, 1],
#                       [1, 2, 7, 6, 3, 5, 4],
#                       [3, 4, 2, 1, 5, 7, 6] ]
# Latin squares have many practical uses, for example in error-correcting-codes and the design of agricultural experiments. See https://en.wikipedia.org/wiki/Latin_square for more details. Sudoku is a 9 x 9 latin square, with additional conditions.
#
# Creating a latin square of any size is fairly straightforward (see the kata Latin Squares). Validating that an arbitrary array is a latin square is slightly trickier, especially if you want to provide helpful feedback messages in case it's not.
#
# Task
# Write a function that validates if an input array is a latin square. It has two parameters, the array and a positive integer m > 1. To help the user with debugging, it should return an appropriate message, as detailed below. It must not modify the input array.
#
# Details
# The input array is guaranteed to be 2D and contain only integers. If it is a valid latin square of size m, the function should return "Valid latin square of size <m>". Otherwise, it should return one of the following messages:
#
# If the input array is not square, the function should return "Array not square"
#
# If the input array is square, but not of size m, the function should return "Array is wrong size". NOTE: When the array is both not square and the wrong size, the first point applies, so "Array not square" should be returned.
#
# If any value between 1 and m in the array occurs more than once in a particular row, the function should identify it and its row by returning "<value> occurs more than once in row <s>". If there are multiple such values, only one should be identified. Row indexes run from 1 to m.
#
# If any value between 1 and m in the array occurs more than once in a particular column, the function should return "<value> occurs more than once in column <t>". If there are multiple such values, only one should be identified. Column indexes run from 1 to m.
#
# If any value in the array is not between 1 and m, the function should identify it and its location by returning "<value> at <row>,<col> is not between 1 and <m>". If there are multiple such values, only one should be identified.
#
# If more than one of the above conditions occur, the function should return one of the appropriate messages. For example, suppose m is 4 and the array is
#
# [ [1, 2, 1, 1],
#   [5, 2, 3, 4],
#   [4, 3, 0, 2, 1],
#   [2, 1, 4, 3] ]
# Then the function can return any of the following:
#
# "Array not square"
# "1 occurs more than once in row 1"
# "2 occurs more than once in column 2"
# "5 at 2,1 is not between 1 and 4"
# "0 at 3,3 is not between 1 and 4"
# Worth Noting
# There is no known easily-computable formula for the number of latin squares of a given size (see https://en.wikipedia.org/wiki/Latin_square - Number of n × n Latin squares).
#
# If you like this kata, you might also be interested in Sudokuboard validator.
#
# STRINGSARRAYS
# Solution
def verify_latin_square(array, m):
    mx_row: int = max(len(row) for row in array)
    mn_row: int = min(len(row) for row in array)
    if (len(array) != mx_row or mx_row != mn_row) and len(array) != m: return 'Array not square'
    if (len(array) != mx_row or mx_row != mn_row): return 'Array not square'
    if len(array) != m: return 'Array is wrong size'
    for row in range(m):
        cur_set: set[int] = set()
        for col in range(m):
            if array[row][col] in cur_set: return f'{array[row][col]} occurs more than once in row {row + 1}'
            elif not 1 <= array[row][col] <= m: return f'{array[row][col]} at {row + 1},{col + 1} is not between 1 and {m}'
            else: cur_set.add(array[row][col])
    for col in range(m):
        cur_set: set[int] = set()
        for row in range(m):
            if array[row][col] in cur_set: return f'{array[row][col]} occurs more than once in column {col + 1}'
            else: cur_set.add(array[row][col])
    return f'Valid latin square of size {m}'