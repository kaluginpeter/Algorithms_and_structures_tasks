# C. Racing
# time limit per test2 seconds
# memory limit per test256 megabytes
# In 2077, a sport called hobby-droning is gaining popularity among robots.
#
# You already have a drone, and you want to win. For this, your drone needs to fly through a course with n
#  obstacles.
#
# The i
# -th obstacle is defined by two numbers li,ri
# . Let the height of your drone at the i
# -th obstacle be hi
# . Then the drone passes through this obstacle if li≤hi≤ri
# . Initially, the drone is on the ground, meaning h0=0
# .
#
# The flight program for the drone is represented by an array d1,d2,…,dn
# , where hi−hi−1=di
# , and 0≤di≤1
# . This means that your drone either does not change height between obstacles or rises by 1
# . You already have a flight program, but some di
#  in it are unknown and marked as −1
# . Replace the unknown di
#  with numbers 0
#  and 1
#  to create a flight program that passes through the entire obstacle course, or report that it is impossible.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# In the first line of each test case, an integer n
#  (1≤n≤2⋅105)
#  is given — the size of the array d
# .
#
# In the second line of each test case, there are n
#  integers d1,d2,…,dn
#  (−1≤di≤1
# ) — the elements of the array d
# . di=−1
#  means that this di
#  is unknown to you.
#
# Next, there are n
#  lines containing 2
#  integers li,ri
#  (0≤li≤ri≤n
# ) — descriptions of the obstacles.
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output n
#  integers d1,d2,…,dn
# , if it is possible to correctly restore the array d
# , or −1
#  if it is not possible.
#
# Example
# InputCopy
# 5
# 4
# 0 -1 -1 1
# 0 4
# 1 2
# 2 4
# 1 4
# 3
# 0 -1 -1
# 0 1
# 2 2
# 0 3
# 2
# -1 -1
# 0 0
# 2 2
# 8
# -1 -1 1 -1 -1 0 0 -1
# 0 0
# 0 1
# 0 2
# 0 2
# 1 3
# 0 4
# 2 5
# 4 5
# 1
# 0
# 1 1
# OutputCopy
# 0 1 1 1
# -1
# -1
# 0 1 1 0 1 0 0 1
# -1
# Note
# In the first test case, one possible answer is d=[0,1,1,1]
# . The array h
#  will be [0,0+1,0+1+1,0+1+1+1]=[0,1,2,3]
# . This array meets the conditions of the problem.
#
# In the second test case, it can be proven that there is no suitable array d
# , so the answer is −1
# .
# Solution
# C++ O(N) O(N) SweepLine Greedy
#include <iostream>
#include <vector>
#include <deque>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int rep = 0; rep < t; ++rep) {
        int n; std::scanf("%d", &n);
        std::vector<int> plan(n, 0);
        for (int i = 0; i < n; ++i) std::scanf("%d", &plan[i]);
        std::vector<std::pair<int, int>> obstacles;
        for (int i = 0; i < n; ++i) {
            int l, r; std::scanf("%d %d", &l, &r);
            obstacles.push_back({l, r});
        }
        int height = 0;
        bool isValid = true;
        std::vector<int> extra;
        for (int i = 0; i < n; ++i) {
            if (plan[i] == 1) ++height;
            int needRise = 0;
            if (obstacles[i].second < height) {
                isValid = false;
                break;
            }
            if (height < obstacles[i].first) {
                needRise += obstacles[i].first - height;
                height = obstacles[i].first;
            }
            extra.push_back(needRise);
        }
        if (!isValid) {
            std::printf("-1\n"); continue;
        }
        int counter = 0;
        for (int i = n - 1; i >= 0; --i) {
            counter += extra[i];
            if (plan[i] == -1) {
                if (counter) {
                    --counter;
                    --height;
                    plan[i] = 1;
                } else plan[i] = 0;
            } else if (plan[i] == 1) --height;
            if (i - 1 >= 0 && obstacles[i - 1].second < height) break;
        }
        if (counter) {
            std::printf("-1\n"); continue;
        }
        for (int i = 0; i < n; ++i) std::printf("%d ", plan[i]);
        std::printf("\n");
    }
}


int main() {
    solution();
}

# Python O(N) O(N) SweepLine Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        plan: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        obstacles: list[tuple[int, int]] = []
        for i in range(n):
            l, r = map(int, sys.stdin.readline().rstrip().split())
            obstacles.append((l, r))
        height: int = 0
        is_valid: bool = True
        extra: list[int] = []
        for i in range(n):
            if plan[i] == 1: height += 1
            need_rise: int = 0
            if obstacles[i][1] < height:
                is_valid = False
                break
            if height < obstacles[i][0]:
                need_rise += obstacles[i][0] - height
                height = obstacles[i][0]
            extra.append(need_rise)
        if not is_valid:
            sys.stdout.write('-1\n')
            continue
        counter: int = 0
        for i in range(n - 1, -1, -1):
            counter += extra[i]
            if plan[i] == -1:
                if counter:
                    counter -= 1
                    height -= 1
                    plan[i] = 1
                else: plan[i] = 0
            elif plan[i] == 1: height -= 1
            if i - 1 >= 0 and obstacles[i - 1][1] < height: break
        if counter:
            sys.stdout.write('-1\n')
            continue
        sys.stdout.write('{}\n'.format(' '.join(map(str, plan))))

if __name__ == '__main__':
    solution()