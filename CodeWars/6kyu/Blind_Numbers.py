# Nicky has had Myopia (Nearsightedness) since he was born. Because he always wears glasses, he really hates digits 00 and he loves digits 1 and 2. He calls numbers, that don't contain 00 (two consecutive zeros), the Blind Numbers. He will give you n, the digit-length of number in 10-adic system, and you need to help him to count how many numbers are there of length n, that only consist of digits 0, 1 and 2 and are not Blind Numbers.
#
# Note📝
# We include 0 in the begin of number also.
#
# The numbers will be very huge, so return the answer modulo 1000000007
#
# Example
# n = 3
#
# The answer is 22. The below list is all 27 possible numbers of length 3, with digits 0-2, and there 5 numbers that contain 00 so we not include those.
#
# [000, 001, 002, 010, 011, 012, 020, 021, 022, 100, 101, 102, 110, 111, 112, 120 121, 122, 200, 201, 202, 210 , 211, 212, 220, 221, 222]
# Constraints
# 1 ≤ n ≤ 500000
#
# MATHEMATICSFUNDAMENTALS
# Solution
def blind_number(n):
    MOD = 1000000007

    dp0, dp1, dp2 = 1, 1, 1

    for i in range(2, n + 1):
        new_dp0 = (dp1 + dp2) % MOD
        new_dp1 = (dp0 + dp1 + dp2) % MOD
        new_dp2 = (dp0 + dp1 + dp2) % MOD

        dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2

    return (dp0 + dp1 + dp2) % MOD