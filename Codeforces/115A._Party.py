# A. Party
# time limit per test3 seconds
# memory limit per test256 megabytes
# A company has n employees numbered from 1 to n. Each employee either has no immediate manager or exactly one immediate manager, who is another employee with a different number. An employee A is said to be the superior of another employee B if at least one of the following is true:
#
# Employee A is the immediate manager of employee B
# Employee B has an immediate manager employee C such that employee A is the superior of employee C.
# The company will not have a managerial cycle. That is, there will not exist an employee who is the superior of his/her own immediate manager.
#
# Today the company is going to arrange a party. This involves dividing all n employees into several groups: every employee must belong to exactly one group. Furthermore, within any single group, there must not be two employees A and B such that A is the superior of B.
#
# What is the minimum number of groups that must be formed?
#
# Input
# The first line contains integer n (1 ≤ n ≤ 2000) — the number of employees.
#
# The next n lines contain the integers pi (1 ≤ pi ≤ n or pi = -1). Every pi denotes the immediate manager for the i-th employee. If pi is -1, that means that the i-th employee does not have an immediate manager.
#
# It is guaranteed, that no employee will be the immediate manager of him/herself (pi ≠ i). Also, there will be no managerial cycles.
#
# Output
# Print a single integer denoting the minimum number of groups that will be formed in the party.
#
# Examples
# InputCopy
# 5
# -1
# 1
# 2
# 1
# -1
# OutputCopy
# 3
# Note
# For the first example, three groups are sufficient, for example:
#
# Employee 1
# Employees 2 and 4
# Employees 3 and 5
# Solution
# C++ O(V + E) O(V + E) Graphs
#include <iostream>
#include <vector>
#include <queue>


void solution() {
    int n;
    std::scanf("%d", &n);
    std::vector<std::vector<int>> child (n + 1, std::vector<int>());
    std::queue<int> q;
    for (int i = 1; i <= n; ++i) {
        int j;
        std::scanf("%d", &j);
        if (j == -1) q.push(i);
        else child[j].push_back(i);
    }
    int groups = 0;
    while (!q.empty()) {
        ++groups;
        int bound = q.size();
        for (int i = 0; i < bound; ++i) {
            int& vertex = q.front();
            q.pop();
            if (!child[vertex].empty()) {
                for (int& employee : child[vertex]) q.push(employee);
            }
        }
    }

    std::printf("%d\n", groups);
}


int main() {
    solution();
}

# Python O(V + E) O(V + E) Graphs
import sys
from collections import deque

def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    child: list[list[int]] = [[] for _ in range(n + 1)]
    queue: deque[int] = deque()
    for i in range(1, n + 1):
        j: int = int(sys.stdin.readline().rstrip())
        if j == -1: queue.append(i)
        else: child[j].append(i)
    groups: int = 0
    while queue:
        groups += 1
        bound: int = len(queue)
        for _ in range(bound):
            vertex: int = queue.popleft()
            if child[vertex]:
                for employee in child[vertex]: queue.append(employee)
    sys.stdout.write('{}\n'.format(groups))


if __name__ == '__main__':
    solution()