# A. Only Pluses
# time limit per test1 second
# memory limit per test256 megabytes
# Kmes has written three integers a
# , b
#  and c
#  in order to remember that he has to give Noobish_Monk a×b×c
#  bananas.
#
# Noobish_Monk has found these integers and decided to do the following at most 5
#  times:
#
# pick one of these integers;
# increase it by 1
# .
# For example, if a=2
# , b=3
#  and c=4
# , then one can increase a
#  three times by one and increase b
#  two times. After that a=5
# , b=5
# , c=4
# . Then the total number of bananas will be 5×5×4=100
# .
#
# What is the maximum value of a×b×c
#  Noobish_Monk can achieve with these operations?
#
# Input
# Each test contains multiple test cases. The first line of input contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases. The description of the test cases follows.
#
# The first and only line of each test case contains three integers a
# , b
#  and c
#  (1≤a,b,c≤10
# ) — Kmes's integers.
#
# Output
# For each test case, output a single integer — the maximum amount of bananas Noobish_Monk can get.
#
# Example
# InputCopy
# 2
# 2 3 4
# 10 1 10
# OutputCopy
# 100
# 600
# Solution
# C++ Simulation O(1) O(1)
#include <iostream>
#include <algorithm>

int maxProductAfterIncrements(int a, int b, int c) {
    int max_product = a * b * c;
    for (int i = 0; i <= 5; ++i) {
        for (int j = 0; j <= 5 - i; ++j) {
            int k = 5 - i - j;
            int current_product = (a + i) * (b + j) * (c + k);
            max_product = std::max(max_product, current_product);
        }
    }

    return max_product;
}

void solution(int t) {
    for (int i = 0; i < t; ++i) {
        int a, b, c;
        std::cin >> a >> b >> c;
        int result = maxProductAfterIncrements(a, b, c);
        std::cout << result << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(1) O(1) Simulation
import sys

def max_product(a: int, b: int, c: int) -> int:
    max_product: int = a * b * c
    for i in range(6):
        j: int = 0
        while j <= 5 - i:
            k: int = 5 - i - j
            current_product: int = (a + i) * (b + j) * (c + k)
            max_product = max(max_product, current_product)
            j += 1
    return max_product

def solution(t: int) -> None:
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(max_product(a, b, c)) + '\n')
if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
