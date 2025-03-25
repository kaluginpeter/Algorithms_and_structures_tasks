# A. Quintomania
# time limit per test1 second
# memory limit per test256 megabytes
# Boris Notkin composes melodies. He represents them as a sequence of notes, where each note is encoded as an integer from 0
#  to 127
#  inclusive. The interval between two notes a
#  and b
#  is equal to |a−b|
#  semitones.
#
# Boris considers a melody perfect if the interval between each two adjacent notes is either 5
#  semitones or 7
#  semitones.
#
# After composing his latest melodies, he enthusiastically shows you his collection of works. Help Boris Notkin understand whether his melodies are perfect.
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of melodies.
#
# Each melody is described by two lines.
#
# The first line contains an integer n
#  (2≤n≤50
# ) — the number of notes in the melody.
#
# The second line contains n
#  integers a1,a2,…,an
#  (0≤ai≤127
# ) — the notes of the melody.
#
# Output
# For each melody, output "YES", if it is perfect; otherwise, output "NO".
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 8
# 2
# 114 109
# 2
# 17 10
# 3
# 76 83 88
# 8
# 38 45 38 80 85 92 99 106
# 5
# 63 58 65 58 65
# 8
# 117 124 48 53 48 43 54 49
# 5
# 95 102 107 114 121
# 10
# 72 77 82 75 70 75 68 75 68 75
# OutputCopy
# YES
# YES
# YES
# NO
# YES
# NO
# YES
# YES
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>
#include <cmath>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<int> nums (n, 0);
        for (int j = 0; j < n; ++j) std::scanf("%d", &nums[j]);
        bool isValid = true;
        for (int j = 1; j < n; ++j) {
            int diff = std::abs(nums[j - 1] - nums[j]);
            if (diff != 5 && diff != 7) {
                isValid = false;
                break;
            }
        }
        std::cout << (isValid? "YES" : "NO") << "\n";
    }
}


int main() {
    solution();
}
# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        sys.stdout.write('{}\n'.format(['NO', 'YES'][all(abs(nums[i - 1] - nums[i]) in {5, 7} for i in range(1, n))]))


if __name__ == '__main__':
    solution()