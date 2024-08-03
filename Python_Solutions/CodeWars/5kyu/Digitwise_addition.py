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