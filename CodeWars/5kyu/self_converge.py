# self_converge
# Goal: Given a number (with a minimum of 3 digits), return the number of iterations it takes to arrive at a derived number that converges on to itself, as per the following Kaprekar routine. As a learning exercise, come up with a solution that uses recursion. The following steps would be applicable to a number that originally had exactly 4 digits.
#
# Initialize a counter to count the number of iterations
# Take any four-digit number n, using at least two different digits.
# Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
# Add as many zeroes so that the width of the original number is maintained.
# Subtract the smaller number from the bigger number. Let us call this nseq.
# Check if nseq (the remainder) from Step 4 equals the previous value of n. If not, increment the iteration counter and go back to step 2 and perform it on the nseq.
# If the number of digits to start with was more than 4, convergence occurs on to a cycle of numbers. Therefore in Step 5, detect this cycle by comparing to not only the previous value, but to all previous values of n.
#
# If there is a match, then return the count of iterations
# If the sequence_number collapses to zero, then return -1
# Converge values
# While 3-digit numbers converge to the same unique number k which is also 3 digits long, all 4-digit numbers also converge to the same unique value k1 which is 4 digits long. However, 5 digit numbers converge to any one of the following values: 53955, 59994, 61974, 62964, 63954, 71973, 74943, 75933, 82962, 83952.
#
# Example
# 1234 -> 4
#
# 1. 4321 - 1234 =  3087 /
# 2. 8730 - 378  =  8352 /
# 3. 8532 - 2358 =  6174 /
# 4. 7641 - 1467 =  6174 // same as previous
# 414 -> 5
#
# 1. 441 - 144 =  297 /
# 2. 972 - 279 =  693 /
# 3. 963 - 369 =  594 /
# 4. 954 - 459 =  495 /
# 5. 954 - 459 =  495 // same as previous
# 50000 -> 4
#
# 1. 50000 - 5      =  49995 /
# 2. 99954 - 45999  =  53955 /  # first
# 3. 95553 - 35559  =  59994 /
# 4. 99954 - 45999  =  53955 /  # 2nd time
# RECURSIONALGORITHMS
# Solution
def convert(n: int, flag: bool = False, zeroes: int = 0) -> int:
    l: list = []
    while n:
        l.append(n % 10)
        n //= 10
    l.sort(reverse=flag)
    ans: int = 0
    for i in l:
        ans = ans * 10 + i
    if flag:
        while ans < int(f'1{"0" * zeroes}'):
            ans *= 10
    return ans


def self_converge(n):
    hs: set = set()
    count: int = 1
    prev_x: int = -1
    zeroes: int = len(str(n)) - 1
    x: int = convert(n, flag=True, zeroes=zeroes) - convert(n)
    while x != prev_x:
        if x > 9999:
            if x in hs: return count
        count += 1
        prev_x = x
        hs.add(prev_x)
        x = convert(x, flag=True, zeroes=zeroes) - convert(x)

    return count