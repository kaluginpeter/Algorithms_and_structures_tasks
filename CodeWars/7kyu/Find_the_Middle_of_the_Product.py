# Given a string of characters, I want the function findMiddle()/find_middle() to return the middle number in the product of each digit in the string.
#
# Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.
#
# Not all strings will contain digits. In this case and the case for any non-strings, return -1.
#
# If the product has an even number of digits, return the middle two digits
#
# Example: 1563 -> 56
#
# NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1
#
# FundamentalsStrings
# Solution
def find_middle(st):
    if not st or not isinstance(st, str): return -1
    prev: int = -1
    for letter in st:
        if letter.isdigit():
            if prev == -1: prev = int(letter)
            else: prev *= int(letter)
    if prev == -1: return -1
    str_prev: str = str(prev)
    if len(str_prev) & 1:
        return int(str_prev[len(str_prev) // 2])
    return int(str_prev[len(str_prev) // 2 - 1:len(str_prev) // 2 + 1])