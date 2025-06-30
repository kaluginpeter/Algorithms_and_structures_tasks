# A. LRC and VIP
# time limit per test1 second
# memory limit per test256 megabytes
#
# You have an array a
#  of size n
#  — a1,a2,…an
# .
#
# You need to divide the n
#  elements into 2
#  sequences B
#  and C
# , satisfying the following conditions:
#
# Each element belongs to exactly one sequence.
# Both sequences B
#  and C
#  contain at least one element.
# gcd
#  (B1,B2,…,B|B|)≠gcd(C1,C2,…,C|C|)
#  ∗
# ∗
# gcd(x,y)
#  denotes the greatest common divisor (GCD) of integers x
#  and y
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains an integer n
#  (2≤n≤100
# ).
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤104
# ).
#
# Output
# For each test case, first output Yes
#  if a solution exists or No
#  if no solution exists. You may print each character in either case, for example YES
#  and yEs
#  will also be accepted.
#
# Only when there is a solution, output n
#  integers on the second line. The i
# -th number should be either 1
#  or 2
# . 1
#  represents that the element belongs to sequence B
#  and 2
#  represents that the element belongs to sequence C
# .
#
# You should guarantee that 1
#  and 2
#  both appear at least once.
#
# Example
# InputCopy
# 3
# 4
# 1 20 51 9
# 4
# 5 5 5 5
# 3
# 1 2 2
# OutputCopy
# Yes
# 2 2 1 1
# No
# Yes
# 1 2 2
# Note
# In the first test case, B=[51,9]
#  and C=[1,20]
# . You can verify gcd(B1,B2)=3≠1=gcd(C1,C2)
# .
#
# In the second test case, it is impossible to find a solution. For example, suppose you distributed the first 3
#  elements to array B
#  and then the last element to array C
# . You have B=[5,5,5]
#  and C=[5]
# , but gcd(B1,B2,B3)=5=gcd(C1)
# . Hence it is invalid.
# Solution
# C++ O(N^2) O(N) Greedy
#include <iostream>
#include <vector>
#include <numeric>

// Standard GCD function
int gcd(int a, int b) {
    while (b) {
        a %= b;
        std::swap(a, b);
    }
    return a;
}

int calculate_gcd_of_vector(const std::vector<int>& vec) {
    if (vec.empty()) return 0;
    int result = vec[0];
    for (size_t i = 1; i < vec.size(); ++i) result = gcd(result, vec[i]);
    return result;
}

void solution() {
    int t;
    std::cin >> t;
    for (int rep = 0; rep < t; ++rep) {
        int n;
        std::cin >> n;
        std::vector<int> a(n);
        bool all_same = true;
        std::cin >> a[0];
        for (int i = 1; i < n; ++i) {
            std::cin >> a[i];
            if (a[i] != a[0]) all_same = false;
        }

        if (all_same) {
            std::cout << "No\n";
            continue;
        }

        std::cout << "Yes\n";
        for (int i = 0; i < n; ++i) {
            std::vector<int> group_c;
            for (int j = 0; j < n; ++j) {
                if (i != j) group_c.push_back(a[j]);
            }
            bool isBreak = false;

            int gcd_b = a[i];
            int gcd_c = calculate_gcd_of_vector(group_c);

            if (gcd_b != gcd_c) {
                for (int j = 0; j < n; ++j) {
                    if (i == j) std::cout << "1 ";
                    else std::cout << "2 ";
                }
                std::cout << "\n";
                isBreak = true;
                break;
            }
            if (isBreak) break;
        }
    }
}


int main() {
    solution();
}

# Python O(N^2) O(N) Greedy
import sys
import math


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        if len(set(nums)) == 1:
            sys.stdout.write('NO\n')
            continue
        sys.stdout.write('YES\n')
        for i in range(n):
            group_c: list[int] = [nums[j] for j in range(n) if i != j]
            is_break: bool = False
            gcd_b: int = nums[i]
            gcd_c: int = math.gcd(*group_c)
            if gcd_b != gcd_c:
                for j in range(n):
                    if i == j: sys.stdout.write('1 ')
                    else: sys.stdout.write('2 ')
                sys.stdout.write('\n')
                is_break = True
                break
            if is_break: break


if __name__ == '__main__':
    solution()
