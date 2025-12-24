# In recreational mathematics, a Keith number or repfigit number (short for repetitive Fibonacci-like digit) is a number in the following integer sequence:
#
# 14, 19, 28, 47, 61, 75, 197, 742, 1104, 1537, 2208, 2580, 3684, 4788, 7385, 7647, 7909, ... (sequence A007629 in the OEIS)
#
# Keith numbers were introduced by Mike Keith in 1987. They are computationally very challenging to find, with only about 100 known.
#
# Implement the code to check if the given number is a Keith number. Return the number number of iteration needed to confirm it; otherwise return false.
#
# Note: 1-digit numbers are not Keith numbers by definition
#
# Examples
# n = 197      # --> [1, 9, 7]
#
# # calculation           iteration
# 1 + 9 + 7 = 17         #    1
# 9 + 7 + 17 = 33        #    2
# 7 + 17 + 33 = 57       #    3
# 17 + 33 + 57 = 107     #    4
# 33 + 57 + 107 = 197    #    5
# As 197 is the same as the initial number, so it's a Keith number: return 5
#
# Another example:
#
# n = 196
#
# # calculation          iteration
# 1 + 9 + 6 = 16        #    1
# ...
# 196 is not a Keith number, so return false
#
# AlgorithmsMathematics
# Solution
def is_keith_number(n):
    if n < 10: return False
    i: int = 0
    digits: list[int] = []
    tmp: int = n
    while n:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    while True:
        i += 1
        if i == 200: break
        x: int = sum(digits)
        digits = digits[1:] + [x]
        if digits[-1] == tmp: return i
    return False