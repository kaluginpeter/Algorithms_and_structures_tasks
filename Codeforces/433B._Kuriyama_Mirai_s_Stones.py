# B. Kuriyama Mirai's Stones
# time limit per test2 seconds
# memory limit per test256 megabytes
# Kuriyama Mirai has killed many monsters and got many (namely n) stones. She numbers the stones from 1 to n. The cost of the i-th stone is vi. Kuriyama Mirai wants to know something about these stones so she will ask you two kinds of questions:
#
# She will tell you two numbers, l and r (1 ≤ l ≤ r ≤ n), and you should tell her .
# Let ui be the cost of the i-th cheapest stone (the cost that will be on the i-th place if we arrange all the stone costs in non-decreasing order). This time she will tell you two numbers, l and r (1 ≤ l ≤ r ≤ n), and you should tell her .
# For every question you should give the correct answer, or Kuriyama Mirai will say "fuyukai desu" and then become unhappy.
#
# Input
# The first line contains an integer n (1 ≤ n ≤ 105). The second line contains n integers: v1, v2, ..., vn (1 ≤ vi ≤ 109) — costs of the stones.
#
# The third line contains an integer m (1 ≤ m ≤ 105) — the number of Kuriyama Mirai's questions. Then follow m lines, each line contains three integers type, l and r (1 ≤ l ≤ r ≤ n; 1 ≤ type ≤ 2), describing a question. If type equal to 1, then you should output the answer for the first question, else you should output the answer for the second one.
#
# Output
# Print m lines. Each line must contain an integer — the answer to Kuriyama Mirai's question. Print the answers to the questions in the order of input.
#
# Examples
# InputCopy
# 6
# 6 4 2 7 2 7
# 3
# 2 3 6
# 1 3 4
# 1 1 6
# OutputCopy
# 24
# 9
# 28
# InputCopy
# 4
# 5 5 2 3
# 10
# 1 2 4
# 2 1 4
# 1 1 1
# 2 1 4
# 2 1 2
# 1 1 1
# 1 3 3
# 1 1 3
# 1 4 4
# 1 2 2
# OutputCopy
# 10
# 15
# 5
# 15
# 5
# 5
# 2
# 12
# 3
# 5
# Note
# Please note that the answers to the questions may overflow 32-bit integer type.
# Solution
# C++ O(NlogN) O(N) Prefix Sum
#include <iostream>
#include <vector>
#include <algorithm>

void solution() {
    int n;
    std::cin >> n;
    std::vector<int> v;
    for (int i = 0; i < n; ++i) {
        int score;
        std::cin >> score;
        v.push_back(score);
    }
    std::vector<long long> firstQuestion;
    for (int idx = 0; idx < n; ++idx) {
        if (idx) {
            firstQuestion.push_back(v[idx] + firstQuestion[idx - 1]);
        } else {
            firstQuestion.push_back(v[idx]);
        }
    }
    std::sort(v.begin(), v.end());
    std::vector<long long> secondQuestion;
    for (int idx = 0; idx < n; ++idx) {
        if (idx) {
            secondQuestion.push_back(v[idx] + secondQuestion[idx - 1]);
        } else {
            secondQuestion.push_back(v[idx]);
        }
    }

    int m;
    std::cin >> m;
    for (int i = 0; i < m; ++i) {
        int t, l, r;
        std::cin >> t >> l >> r;
        if (t == 1) {
            std::cout << (l - 1? firstQuestion[r - 1] - firstQuestion[l - 2] : firstQuestion[r - 1]);
        } else {
            std::cout << (l - 1? secondQuestion[r - 1] - secondQuestion[l - 2] : secondQuestion[r - 1]);
        }
        std::cout << "\n";
    }
}


int main() {
    solution();
}

# Python O(NlogN) O(N) Prefix Sum
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    v: list = list(map(int, sys.stdin.readline().rstrip().split()))
    first_question: list = []
    for idx in range(n):
        if idx:
            first_question.append(first_question[-1] + v[idx])
        else:
            first_question.append(v[idx])
    second_question: list = []
    v.sort()
    for idx in range(n):
        if idx:
            second_question.append(second_question[-1] + v[idx])
        else:
            second_question.append(v[idx])
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        t, l, r = map(int, sys.stdin.readline().rstrip().split())
        if t == 1:
            sys.stdout.write(str(first_question[r - 1] - (first_question[l - 2] if l - 1 else 0)))
        else:
            sys.stdout.write(str(second_question[r - 1] - (second_question[l - 2] if l - 1 else 0)))
        sys.stdout.write('\n')


if __name__ == '__main__':
    solution()
