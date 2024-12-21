# A. Two Elevators
# time limit per test1 second
# memory limit per test256 megabytes
# Vlad went into his appartment house entrance, now he is on the 1
# -th floor. He was going to call the elevator to go up to his apartment.
#
# There are only two elevators in his house. Vlad knows for sure that:
#
# the first elevator is currently on the floor a
#  (it is currently motionless),
# the second elevator is located on floor b
#  and goes to floor c
#  (b≠c
# ). Please note, if b=1
# , then the elevator is already leaving the floor 1
#  and Vlad does not have time to enter it.
# If you call the first elevator, it will immediately start to go to the floor 1
# . If you call the second one, then first it will reach the floor c
#  and only then it will go to the floor 1
# . It takes |x−y|
#  seconds for each elevator to move from floor x
#  to floor y
# .
#
# Vlad wants to call an elevator that will come to him faster. Help him choose such an elevator.
#
# Input
# The first line of the input contains the only t
#  (1≤t≤104
# ) — the number of test cases.
#
# This is followed by t
#  lines, three integers each a
# , b
#  and c
#  (1≤a,b,c≤108
# , b≠c
# ) — floor numbers described in the statement.
#
# Output
# Output t
#  numbers, each of which is the answer to the corresponding test case. As an answer, output:
#
# 1
# , if it is better to call the first elevator;
# 2
# , if it is better to call the second one;
# 3
# , if it doesn't matter which elevator to call (both elevators will arrive in the same time).
# Example
# InputCopy
# 3
# 1 2 3
# 3 1 2
# 3 2 1
# OutputCopy
# 1
# 3
# 2
# Note
# In the first test case of the example, the first elevator is already on the floor of 1
# .
#
# In the second test case of the example, when called, the elevators would move as follows:
#
# At the time of the call, the first elevator is on the floor of 3
# , and the second one is on the floor of 1
# , but is already going to another floor;
# in 1
#  second after the call, the first elevator would be on the floor 2
# , the second one would also reach the floor 2
#  and now can go to the floor 1
# ;
# in 2
#  seconds, any elevator would reach the floor 1
# .
# In the third test case of the example, the first elevator will arrive in 2
#  seconds, and the second in 1
# .
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int a, b, c;
        std::cin >> a >> b >> c;
        int aTime = a - 1;
        int bTime = (b >= c? b - c : c - b) + c - 1;
        if (aTime < bTime) {
            std::cout << 1;
        } else if (bTime < aTime) {
            std::cout << 2;
        } else {
            std::cout << 3;
        }
        std::cout << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}
# Python O(1) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        a_time: int = a - 1
        b_time: int = (b - c if b >= c else c - b) + c - 1
        sys.stdout.write(('1' if a_time < b_time else '2' if b_time < a_time else '3') + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
