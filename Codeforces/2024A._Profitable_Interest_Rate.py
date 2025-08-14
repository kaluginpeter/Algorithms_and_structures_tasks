# A. Profitable Interest Rate
# time limit per test1 second
# memory limit per test256 megabytes
# Alice has a
#  coins. She can open a bank deposit called "Profitable", but the minimum amount required to open this deposit is b
#  coins.
#
# There is also a deposit called "Unprofitable", which can be opened with any amount of coins. Alice noticed that if she opens the "Unprofitable" deposit with x
#  coins, the minimum amount required to open the "Profitable" deposit decreases by 2x
#  coins. However, these coins cannot later be deposited into the "Profitable" deposit.
#
# Help Alice determine the maximum number of coins she can deposit into the "Profitable" deposit if she first deposits some amount of coins (possibly 0
# ) into the "Unprofitable" deposit. If Alice can never open the "Profitable" deposit, output 0
# .
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# A single line of each test case contains two integers a
#  and b
#  (1≤a,b≤109
# ) — the number of coins Alice has and the initial minimum amount required to open the "Profitable" deposit.
#
# Output
# For each test case, output a single integer — the maximum number of coins that Alice can deposit into the "Profitable" deposit. If Alice can never open the "Profitable" deposit, output 0
# .
#
# Example
# InputCopy
# 5
# 10 5
# 7 9
# 5 100
# 1 1
# 1 2
# OutputCopy
# 10
# 5
# 0
# 1
# 0
# Note
# In the first test case, a≥b
# , so Alice can immediately open the "Profitable" deposit with all 10
#  coins.
#
# In the second test case, Alice can open the "Unprofitable" deposit with 2
#  coins. Then she will have 5
#  coins left, but the minimum amount required to open the "Profitable" deposit will decrease by 4
#  coins, making it equal to 5
#  coins. Thus, Alice will be able to open the "Profitable" deposit with 5
#  coins.
#
# In the third test case, Alice will not be able to open the "Profitable" deposit.
# Solution
# C++ O(logN) O(1) Math BinarySearch
#include <iostream>


void solution() {
    int a, b;
    std::cin >> a >> b;
    if (a >= b) {
        std::cout << a << std::endl;
        return;
    }
    int output = 0, left = 0, right = a;
    while (left <= right) {
        int middle = left + ((right - left) >> 1);
        if (b - middle * 2 > a - middle) left = middle + 1;
        else if (a - middle > output) {
            output = a - middle;
            right = middle - 1;
        } else left = middle + 1;
    }
    std::cout << output << std::endl;

}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(logN) O(1) Math BinarySearch
import sys


def solution() -> None:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a >= b:
        sys.stdout.write('{}\n'.format(a))
        return
    left: int = 0
    right: int = a
    output: int = 0
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if b - 2 * middle > a - middle: left = middle + 1
        elif a - middle > output:
            output = a - middle
            right = middle - 1
        else: left = middle + 1
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()