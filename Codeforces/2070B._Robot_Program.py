# B. Robot Program
# time limit per test2 seconds
# memory limit per test512 megabytes
# There is a robot on the coordinate line. Initially, the robot is located at the point x
#  (x≠0
# ). The robot has a sequence of commands of length n
#  consisting of characters, where L represents a move to the left by one unit (from point p
#  to point (p−1)
# ) and R represents a move to the right by one unit (from point p
#  to point (p+1)
# ).
#
# The robot starts executing this sequence of commands (one command per second, in the order they are presented). However, whenever the robot reaches the point 0
# , the counter of executed commands is reset (i. e. it starts executing the entire sequence of commands from the very beginning). If the robot has completed all commands and is not at 0
# , it stops.
#
# Your task is to calculate how many times the robot will enter the point 0
#  during the next k
#  seconds.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of a test case contains three integers n
# , x
#  and k
#  (1≤n≤2⋅105
# ; −n≤x≤n
# ; n≤k≤1018
# ).
#
# The second line of a test case contains a string s
#  consisting of n
#  characters L and/or R.
#
# Additional constraint on the input: the sum of n
#  over all test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, print a single integer — the number of times the robot will enter the point 0
#  during the next k
#  seconds.
#
# Example
# InputCopy
# 6
# 3 2 6
# LLR
# 2 -1 8
# RL
# 4 -2 5
# LRRR
# 5 3 7
# LRRLL
# 1 1 1
# L
# 3 -1 4846549234412827
# RLR
# OutputCopy
# 1
# 4
# 1
# 0
# 1
# 2423274617206414
# Note
# In the first example, the robot moves as follows: 2→1→0–→−1→−2→−1
# . The robot has completed all instructions from the sequence and is not at 0
# . So it stops after 5
#  seconds and the point 0
#  is entered once.
#
# In the second example, the robot moves as follows: −1→0–→1→0–→1→0–→1→0–→1
# . The robot worked 8
#  seconds and the point 0
#  is entered 4
#  times.
#
# In the third example, the robot moves as follows: −2→−3→−2→−1→0–→−1
# . The robot worked 5
#  seconds and the point 0
#  is entered once.
#
# In the fourth example, the robot moves as follows: 3→2→3→4→3→2
# . The robot has completed all instructions from the sequence and is not at 0
# . So it stops after 5
#  seconds, without reaching the point 0
# .
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    int n, x;
    long long k;
    std::cin >> n >> x >> k;
    std::string path;
    std::cin >> path;
    int loopSize = -1, start = 0, seconds = -1;
    for (int i = 0; i < n; ++i) {
        if (path[i] == 'L') --x;
        else ++x;
        if (!x) {
            seconds = i + 1;
            break;
        }
    }
    if (seconds == -1 || seconds > k) {
        std::cout << 0 << std::endl;
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (path[i] == 'L') --start;
        else ++start;
        if (!start) {
            loopSize = i + 1;
            break;
        }
    }
    if (loopSize == -1) {
        std::cout << 1 << std::endl;
        return;
    }
    k -= seconds;
    std::cout << 1 + k / loopSize << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n, x, k = map(int, sys.stdin.readline().rstrip().split())
    path: str = sys.stdin.readline().rstrip()
    seconds: int = 0
    for i in range(n):
        if path[i] == 'L': x -= 1
        else: x += 1
        if not x:
            seconds = i + 1
            break
    if not seconds or seconds > k:
        sys.stdout.write('0\n')
        return
    loop_size: int = 0
    start: int = 0
    for i in range(n):
        if path[i] == 'L': start -= 1
        else: start += 1
        if not start:
            loop_size = i + 1
            break
    if not loop_size:
        sys.stdout.write('1\n')
        return
    k -= seconds
    sys.stdout.write('{}\n'.format(1 + k // loop_size))

if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()