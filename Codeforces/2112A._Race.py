# A. Race
# time limit per test2 seconds
# memory limit per test256 megabytes
# Alice and Bob participate in a game TV show. When the game starts, the prize will be dropped to a certain point, and whoever gets to it first will get the prize.
#
# Alice decided that she would start running from point a
# . Bob, however, has not yet chosen his starting position.
#
# Bob knows that the prize could drop either at point x
#  or at point y
# . He also knows that he can reach the prize faster than Alice if the distance from his starting position to the prize is strictly less than the distance from Alice's starting position to the prize. The distance between any two points c
#  and d
#  is calculated as |c−d|
# .
#
# Your task is to determine whether Bob can choose an integer point that is guarantee to get to the prize faster, regardless of where it appears (at point x
#  or y
# ). Bob can choose any integer point, except for a
#  (in particular, he can choose to start in point x
# , point y
# , or any other point, but not a
# ).
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The only line of each test case contains three integers a
# , x
# , y
#  (1≤a,x,y≤100
# ). Points a
# , x
# , and y
#  are pairwise distinct.
#
# Output
# For each test case, print "YES" (case insensitive) if Bob can choose an integer point that is guarantee to get to the prize faster, regardless of where it appears. Otherwise, print "NO" (case insensitive).
#
# Example
# InputCopy
# 3
# 1 3 4
# 5 3 1
# 3 1 5
# OutputCopy
# YES
# YES
# NO
# Note
# In the first example, Bob can choose point 4
# . If the prize will be at point x
# , then Bob's distance is |4−3|=1
#  and Alice's distance is |1−3|=2
# . If the prize will be at point y
# , then Bob's distance is |4−4|=0
#  and Alice's distance is |1−4|=3
# .
#
# In the second example, Bob can choose point 2
# . If the prize will be at point x
# , then Bob's distance is |2−3|=1
#  and Alice's distance is |5−3|=2
# . If the prize will be at point y
# , then Bob's distance is |2−1|=1
#  and Alice's distance is |5−1|=4
# .
#
# In the third example, Bob cannot choose a point to guarantee his victory.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int a, x, y;
        std::cin >> a >> x >> y;
        if ((x < a && y > a) || (y < a && x > a)) {
            std::cout << "NO\n";
            continue;
        }
        int alice = std::max(std::abs(a - x), std::abs(a - y));
        int bob = std::abs(x - y);
        bob = bob / 2 + (bob & 1);

        std::cout << (alice > bob? "YES" : "NO") << std::endl;
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a, x, y = map(int, sys.stdin.readline().rstrip().split())
        if (x < a and y > a) or (y < a and x > a):
            sys.stdout.write('NO\n')
            continue
        alice: int = max(abs(a - x), abs(a - y))
        bob: int = abs(x - y)
        bob = bob // 2 + (bob & 1)
        sys.stdout.write('{}\n'.format(['NO', 'YES'][alice > bob]))



if __name__ == '__main__':
    solution()