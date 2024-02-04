# An array is defined to be odd-heavy if it contains at least one odd element and every element whose value is odd is greater than every even-valued element.
#
# eg.
#
# Array [11,4,9,2,8] is odd-heavy,
# because its odd elements [11,9] are greater than all the even elements [4,2,8]
#
# Array [11,4,9,2,3,10] is not odd-heavy,
# because one of its even elements (10 from [4,2,10]) is greater than two of
# its odd elements (9 and 3 from [11,9,3])
#
# Array [] is not odd-heavy,
# because it does not contain any odd numbers
#
# Array [3] is odd-heavy,
# because it does not contain any even numbers.
# write a function called isOddHeavy or is_odd_heavy that accepts an integer array and returns true if the array is odd-heavy else return false.
#
# ARRAYSFUNDAMENTALS
# Solution
def is_odd_heavy(arr):
    arr.sort()
    x, y = float('inf'), float('-inf')
    for i in arr:
        if i % 2 != 0:
            x = i
            break
    for i in arr[::-1]:
        if i % 2 == 0:
            y = i
            break
    if x != float('inf'):
        return x > y
    return False