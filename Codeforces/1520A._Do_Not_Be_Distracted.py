# A. Do Not Be Distracted!
# time limit per test1 second
# memory limit per test256 megabytes
# Polycarp has 26
#  tasks. Each task is designated by a capital letter of the Latin alphabet.
#
# The teacher asked Polycarp to solve tasks in the following way: if Polycarp began to solve some task, then he must solve it to the end, without being distracted by another task. After switching to another task, Polycarp cannot return to the previous task.
#
# Polycarp can only solve one task during the day. Every day he wrote down what task he solved. Now the teacher wants to know if Polycarp followed his advice.
#
# For example, if Polycarp solved tasks in the following order: "DDBBCCCBBEZ", then the teacher will see that on the third day Polycarp began to solve the task 'B', then on the fifth day he got distracted and began to solve the task 'C', on the eighth day Polycarp returned to the task 'B'. Other examples of when the teacher is suspicious: "BAB", "AABBCCDDEEBZZ" and "AAAAZAAAAA".
#
# If Polycarp solved the tasks as follows: "FFGZZZY", then the teacher cannot have any suspicions. Please note that Polycarp is not obligated to solve all tasks. Other examples of when the teacher doesn't have any suspicious: "BA", "AFFFCC" and "YYYYY".
#
# Help Polycarp find out if his teacher might be suspicious.
#
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ). Then t
#  test cases follow.
#
# The first line of each test case contains one integer n
#  (1≤n≤50
# ) — the number of days during which Polycarp solved tasks.
#
# The second line contains a string of length n
# , consisting of uppercase Latin letters, which is the order in which Polycarp solved the tasks.
#
# Output
# For each test case output:
#
# "YES", if the teacher cannot be suspicious;
# "NO", otherwise.
# You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes and YES are all recognized as positive answer).
#
# Example
# inputCopy
# 5
# 3
# ABA
# 11
# DDBBCCCBBEZ
# 7
# FFGZZZY
# 1
# Z
# 2
# AB
# outputCopy
# NO
# NO
# YES
# YES
# YES
# Solution
# Python O(N) O(N) Hashset
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        tasks: str = sys.stdin.readline().rstrip()
        hashset: set = set()
        hashset.add(tasks[0])
        for idx in range(1, n):
            if tasks[idx] in hashset and tasks[idx] != tasks[idx - 1]:
                print('NO')
                break
            hashset.add(tasks[idx])
        else:
            print('YES')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(N) O(N) HashSet
#include <iostream>
#include <string>
#include <unordered_set>

int main() {
    int t;
    std::cin >> t;
    for (size_t i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::unordered_set<char> storage;
        std::string line;
        std::getline(std::cin, line);
        std::getline(std::cin, line);
        bool is_suspicious = true;
        storage.insert(line[0]);
        for (size_t j = 1; j < n; ++j) {
            if (storage.count(line[j]) && line[j] != line[j - 1]) {
                std::cout << "NO" << std::endl;
                is_suspicious = false;
                break;
            }
            storage.insert(line[j]);
        }
        if (is_suspicious) {
            std::cout << "YES" << std::endl;
        }
    }
}