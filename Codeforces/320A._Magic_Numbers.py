# A. Magic Numbers
# time limit per test2 seconds
# memory limit per test256 megabytes
# A magic number is a number formed by concatenation of numbers 1, 14 and 144. We can use each of these numbers any number of times. Therefore 14144, 141414 and 1411 are magic numbers but 1444, 514 and 414 are not.
#
# You're given a number. Determine if it is a magic number or not.
#
# Input
# The first line of input contains an integer n, (1 ≤ n ≤ 109). This number doesn't contain leading zeros.
#
# Output
# Print "YES" if n is a magic number or print "NO" if it's not.
#
# Examples
# InputCopy
# 114114
# OutputCopy
# YES
# InputCopy
# 1111
# OutputCopy
# YES
# InputCopy
# 441231
# OutputCopy
# NO
# Solution
# C++ O(N) O(1) Simulation
#include <iostream>
#include <string>


void solution() {
    std::string n;
    std::cin >> n;
    bool isValid = true;
    int i = 0;
    for (int j = 0; j < n.size(); ++j) {
        if (n[j] != '4') {
            if (n[j] != '1') {
                isValid = false;
                break;
            }
            i = j + 1;
        } else if ((j - i + 1 == 3) || (j == 0)) {
            isValid = false;
            break;
        }
    }
    std::cout << (isValid? "YES" : "NO") << "\n";
}


int main() {
    solution();
}

# Python O(N) O(1) Simulation
import sys


def solution() -> None:
    n: str = sys.stdin.readline().rstrip()
    is_valid: bool = True
    i: int = 0
    for j in range(len(n)):
        if n[j] != '4':
            if n[j] != '1':
                is_valid = False
                break
            i = j + 1
        elif j - i + 1 == 3 or j == 0:
            is_valid = False
            break
    sys.stdout.write(['NO', 'YES'][is_valid] + '\n')


if __name__ == '__main__':
    solution()
