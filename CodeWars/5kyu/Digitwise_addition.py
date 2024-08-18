# Digitwise addition is a special kind of addition where instead of adding 1 normally to the number, it adds 1 to every digit of that number. If the digit is a 9, we replace it with a "10" without carrying over to the next digit.
#
# Examples:
#
# 123 -> 234
#
# 910 -> 1021
#
# 789 -> 8910
# Program a function that takes two numbers, N and K, and outputs the number of digits in N after applying Digitwise addition K times. Since the answer can be very large, return the answer modulo 10 ** 9 + 7
#
# Specifications: 1 <= N <= 10^9, 1 <= K <= 10^5
#
# Example 1:
#
# digitwise_addition(9812, 2) -> 6
#
# # Explanation:
# # 9812 -> 10923 -> 211034 -> 6 digits
# Example 2:
#
# digitwise_addition(9899, 3) -> 8
#
# # Explanation:
# # 9899 -> 1091010 -> 21102121 -> 32213232 -> 8 digits
# Subtask 1: K <= 20, 30 tests
#
# Subtask 2: K <= 50, 20 tests
#
# Subtask 3: K <= 10^5, 50 tests
#
# ALGORITHMSMATHEMATICS
# Solution
def digitwise_addition(N, K):
    MOD = 10 ** 9 + 7

    # Initialize a list to store the mappings for each digit
    addition = [
        [1],  # 0 -> 1
        [2],  # 1 -> 2
        [3],  # 2 -> 3
        [4],  # 3 -> 4
        [5],  # 4 -> 5
        [6],  # 5 -> 6
        [7],  # 6 -> 7
        [8],  # 7 -> 8
        [9],  # 8 -> 9
        [1, 0]  # 9 -> 1, 0
    ]

    # Initialize a count list to keep track of the occurrences of each digit
    count = [0] * 10
    for digit in str(N):
        count[int(digit)] += 1

    # Iterate K times to simulate the process
    for _ in range(K):
        new_count = [0] * 10
        for digit in range(10):
            for new_digit in addition[digit]:
                new_count[new_digit] = (new_count[new_digit] + count[digit]) % MOD
        count = new_count

    # Sum the counts of all digits
    total_count = sum(count) % MOD

    return total_count