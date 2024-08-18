# Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:
#
# ['XOOXO',
#  'XOOXO',
#  'OOOXO',
#  'XXOXO',
#  'OXOOO']
# which represents:
#
# should return: "Total land perimeter: 24".
#
# Following input:
#
# ['XOOO',
#  'XOXO',
#  'XOXO',
#  'OOXX',
#  'OOOO']
# which represents:
#
# should return: "Total land perimeter: 18"
#
# FUNDAMENTALS
# Solution
def land_perimeter(arr):
    count: int = 0
    moves: list[list[int, int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    arr = ['s' + i + 's' for i in arr]
    arr.append('s' * (len(arr[0])))
    arr.insert(0, 's' * (len(arr[0])))
    for rows in range(len(arr)):
        for column in range(len(arr[0])):
            if arr[rows][column] == 'X':
                for move in moves:
                    if arr[rows + move[0]][column + move[1]] != 'X':
                        count += 1
    return f'Total land perimeter: {count}'