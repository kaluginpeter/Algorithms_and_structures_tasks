# The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details
#
# 8 + 1 = 9 and 92 = 81
#
# 512 = 5 + 1 + 2 = 8 and 83 = 512
#
# We need to make a function that receives a number as argument n and returns the n-th term of this sequence of numbers.
#
# Examples (input --> output)
# 1 --> 81
#
# 2 --> 512
# Happy coding!
#
# AlgorithmsMathematicsSortingData StructuresFundamentals
# Solution
dp: list[int] = []

def digit_sum(x: int) -> int:
    return sum(map(int, str(x)))

def pow_sum_dig_term(n: int) -> int:
    global dp
    if len(dp) >= n:
        return dp[n - 1]

    candidates = set(dp)
    for s in range(2, 200):
        val = s * s
        for k in range(2, 15):
            if digit_sum(val) == s:
                candidates.add(val)
            val *= s

    dp = sorted(candidates)
    return dp[n - 1]