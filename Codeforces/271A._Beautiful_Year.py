# A. Beautiful Year
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.
#
# Now you are suggested to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.
#
# Input
# The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.
#
# Output
# Print a single integer — the minimum year number that is strictly larger than y and all it's digits are distinct. It is guaranteed that the answer exists.
#
# Examples
# inputCopy
# 1987
# outputCopy
# 2013
# inputCopy
# 2013
# outputCopy
# 2014
# Solution Simulation O(N) O(1)
import sys

def check(year: int) -> bool:
    identity: set = set()
    _year = year
    while _year:
        digit = _year % 10
        if digit in identity:
            return False
        identity.add(digit)
        _year //= 10
    return True

def solution(current_year: int) -> str:
    year = current_year + 1
    while True:
        if check(year):
            return str(year)
        year += 1
if __name__ == '__main__':
    current_year: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(current_year))