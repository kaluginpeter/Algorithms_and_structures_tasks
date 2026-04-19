# Seven is a hungry number and its favourite food is number 9. Whenever it spots 9 through the hoops of 8, it eats it! Well, not anymore, because you are going to help the 9 by locating that particular sequence (7,8,9) in an array of digits and tell 7 to come after 9 instead. Seven "ate" nine, no more! (If 9 is not in danger, just return the same array)
#
# Regular ExpressionsFundamentals
# Solution
def hungry_seven(digits: list[int]) -> list[int]:
    while True:
        f = False
        i = 0
        while i < len(digits) - 2:
            if digits[i:i+3] == [7, 8, 9]:
                digits[i:i+3] = [8, 9, 7]
                f = True
                i = max(i - 2, 0)
            else: i += 1
        if not f: break
    return digits