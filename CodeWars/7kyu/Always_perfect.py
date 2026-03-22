# While surfing in web I found interesting math problem called "Always perfect". That means if you add 1 to the product of four consecutive numbers the answer is ALWAYS a perfect square. For example we have: 1,2,3,4 and the product will be 1X2X3X4=24. If we add 1 to the product that would become 25, since the result number is a perfect square the square root of 25 would be 5.
#
# So now lets write a function which takes numbers separated by commas in string format and returns the number which is a perfect square and the square root of that number.
#
# If string contains other characters than number or it has more or less than 4 numbers separated by comma function returns "incorrect input".
#
# If string contains 4 numbers but not consecutive it returns "not consecutive".
#
# StringsArraysMathematicsRegular ExpressionsFundamentals
# Solution
def check_root(strng):
    parts = strng.split(',')
    if len(parts) != 4: return "incorrect input"
    nums = []
    for p in parts:
        try: nums.append(int(p))
        except: return "incorrect input"
    nums.sort()
    for i in range(3):
        if nums[i] + 1 != nums[i + 1]: return "not consecutive"
    n = nums[0]
    root = n*n + 3*n + 1
    square = root * root
    return f"{square}, {abs(root)}"