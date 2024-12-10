# Task
# Get the digits sum of nth number from the Look-and-Say sequence(1-based).
#
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
#
# Input/Output
# [input] integer n
#
# nth number in the sequence to get, where 1 <= n <= 55 and n=1 is "1".
#
# [output] an integer
#
# The sum of digits in nth number from the Look-and-Say sequence.
#
# Example
# For n = 2, the output should be 2.
#
# "11" --> 1 + 1 --> 2
#
# For n = 3, the output should be 3.
#
# "21" --> 2 + 1 --> 3
#
# For n = 4, the output should be 5.
#
# "1211" --> 1 + 2 + 1 + 1 --> 5
#
# Puzzles
# Solution
def look_and_say(start: str) -> str:
    output: list[str] = []
    left: int = 0
    right: int = 0
    while right < len(start):
        while right < len(start) and start[left] == start[right]:
            right += 1
        output.append(str(right - left))
        output.append(str(start[left]))
        left = right
    return ''.join(output)
memo: dict[int, int] = dict()
def look_and_say_and_sum(n):
    if n in memo:
        return memo[n]
    start: str = '1'
    memo[1] = 1
    for _ in range(1, n):
        start = look_and_say(start)
        memo[_ + 1] = sum(int(num) for num in start)
    return memo[n]