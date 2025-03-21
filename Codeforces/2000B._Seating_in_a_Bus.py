# B. Seating in a Bus
# time limit per test2 seconds
# memory limit per test256 megabytes
# In Berland, a bus consists of a row of n
#  seats numbered from 1
#  to n
# . Passengers are advised to always board the bus following these rules:
#
# If there are no occupied seats in the bus, a passenger can sit in any free seat;
# Otherwise, a passenger should sit in any free seat that has at least one occupied neighboring seat. In other words, a passenger can sit in a seat with index i
#  (1≤i≤n
# ) only if at least one of the seats with indices i−1
#  or i+1
#  is occupied.
# Today, n
#  passengers boarded the bus. The array a
#  chronologically records the seat numbers they occupied. That is, a1
#  contains the seat number where the first passenger sat, a2
#  — the seat number where the second passenger sat, and so on.
#
# You know the contents of the array a
# . Determine whether all passengers followed the recommendations.
#
# For example, if n=5
# , and a
#  = [5,4,2,1,3
# ], then the recommendations were not followed, as the 3
# -rd passenger sat in seat number 2
# , while the neighboring seats with numbers 1
#  and 3
#  were free.
#
# Input
# The first line of input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The following describes the input test cases.
#
# The first line of each test case contains exactly one integer n
#  (1≤n≤2⋅105
# ) — the number of seats in the bus and the number of passengers who boarded the bus.
#
# The second line of each test case contains n
#  distinct integers ai
#  (1≤ai≤n
# ) — the seats that the passengers occupied in chronological order.
#
# It is guaranteed that the sum of n
#  values across all test cases does not exceed 2⋅105
# , and that no passenger sits in an already occupied seat.
#
# Output
# For each test case, output on a separate line:
#
# "YES", if all passengers followed the recommendations;
# "NO" otherwise.
# You may output the answer in any case (for example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as a positive answer).
#
# Example
# InputCopy
# 4
# 5
# 5 4 2 1 3
# 3
# 2 3 1
# 4
# 2 3 1 4
# 5
# 1 2 3 5 4
# OutputCopy
# NO
# YES
# YES
# NO
# Note
# The first test case is explained in the problem statement.
# Solution
# C++ O(N) O(1) Two Pointers
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        int left = 0;
        int right = 0;
        bool isValid = true;
        for (int idx = 0; idx < n; ++idx) {
            int seat;
            std::scanf("%d", &seat);
            if (!idx) {
                left = seat;
                right = seat;
                continue;
            }
            if ((seat != left - 1) && (seat != right + 1)) isValid = false;
            else if (seat == left - 1) left = seat;
            else right = seat;
        }
        std::cout << (isValid? "YES" : "NO") << "\n";
    }
}


int main() {
    solution();
}
# Python O(N) O(1) TwoPointers
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        left = right = 0
        is_valid: bool = True
        for idx in range(n):
            seat: int = next(nums)
            if not idx:
                left = right = seat
                continue
            elif seat != left - 1 and seat != right + 1:
                is_valid = False
            elif seat == left - 1: left -= 1
            else: right += 1
        sys.stdout.write('{}\n'.format('YES' if is_valid else 'NO'))


if __name__ == '__main__':
    solution()