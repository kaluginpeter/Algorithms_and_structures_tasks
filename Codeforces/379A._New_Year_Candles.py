# A. New Year Candles
# time limit per test1 second
# memory limit per test256 megabytes
# Vasily the Programmer loves romance, so this year he decided to illuminate his room with candles.
#
# Vasily has a candles.When Vasily lights up a new candle, it first burns for an hour and then it goes out. Vasily is smart, so he can make b went out candles into a new candle. As a result, this new candle can be used like any other new candle.
#
# Now Vasily wonders: for how many hours can his candles light up the room if he acts optimally well? Help him find this number.
#
# Input
# The single line contains two integers, a and b (1 ≤ a ≤ 1000; 2 ≤ b ≤ 1000).
#
# Output
# Print a single integer — the number of hours Vasily can light up the room for.
#
# Examples
# InputCopy
# 4 2
# OutputCopy
# 7
# InputCopy
# 6 3
# OutputCopy
# 8
# Note
# Consider the first sample. For the first four hours Vasily lights up new candles, then he uses four burned out candles to make two new ones and lights them up. When these candles go out (stop burning), Vasily can make another candle. Overall, Vasily can light up the room for 7 hours.
# Solution
# C++ O(logN) O(1) Math
#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    int total_hours = 0;
    int burnt_out = 0;
    while (a > 0) {
        total_hours += a;
        burnt_out += a;

        a = burnt_out / b;
        burnt_out = burnt_out % b;
    }
    std::cout << total_hours << std::endl;
}

# Python O(logN) O(1) Math
import sys


def solution(a: int, b: int) -> str:
    total_hours: int = 0
    burn_out: int = 0
    while a > 0:
        total_hours += a
        burn_out += a
        a = burn_out // b
        burn_out %= b
    return str(total_hours)


if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(a, b))
