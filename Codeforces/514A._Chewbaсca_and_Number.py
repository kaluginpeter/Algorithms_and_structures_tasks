# A. Chewbaсca and Number
# time limit per test1 second
# memory limit per test256 megabytes
# Luke Skywalker gave Chewbacca an integer number x. Chewbacca isn't good at numbers but he loves inverting digits in them. Inverting digit t means replacing it with digit 9 - t.
#
# Help Chewbacca to transform the initial number x to the minimum possible positive number by inverting some (possibly, zero) digits. The decimal representation of the final number shouldn't start with a zero.
#
# Input
# The first line contains a single integer x (1 ≤ x ≤ 1018) — the number that Luke Skywalker gave to Chewbacca.
#
# Output
# Print the minimum possible positive number that Chewbacca can obtain after inverting some digits. The number shouldn't contain leading zeroes.
#
# Examples
# inputCopy
# 27
# outputCopy
# 22
# inputCopy
# 4545
# outputCopy
# 4444
# Solution
# Python O(N) O(1) Math Greedy String
from typing import List
import sys


def solution(n: str) -> None:
    answer: List[str] = []
    for index in range(len(n)):
        current_number: int = int(n[index])
        minimum_number: int = min(current_number, 9 - current_number)
        if index == 0 and minimum_number == 0:
            minimum_number = current_number
        answer.append(str(minimum_number))
    print(''.join(answer))


if __name__ == '__main__':
    n: str = sys.stdin.readline().rstrip()
    solution(n)

# C++ O(N) O(1) Math Greedy String
#include <iostream>
#include <string>

int main() {
    std::string init_number;
    std::cin >> init_number;
    std::string answer = "";
    for (size_t index = 0; index < init_number.size(); ++index) {
        int current_number = init_number[index] - '0';
        int minimum_number = std::min(current_number, 9 - current_number);
        if (index == 0 && minimum_number == 0) {
            minimum_number = current_number;
        }
        answer += std::to_string(minimum_number);

    }
    std::cout << answer << std::endl;
}