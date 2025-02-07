# A. Line Trip
# time limit per test2 seconds
# memory limit per test256 megabytes
# There is a road, which can be represented as a number line. You are located in the point 0
#  of the number line, and you want to travel from the point 0
#  to the point x
# , and back to the point 0
# .
#
# You travel by car, which spends 1
#  liter of gasoline per 1
#  unit of distance travelled. When you start at the point 0
# , your car is fully fueled (its gas tank contains the maximum possible amount of fuel).
#
# There are n
#  gas stations, located in points a1,a2,…,an
# . When you arrive at a gas station, you fully refuel your car. Note that you can refuel only at gas stations, and there are no gas stations in points 0
#  and x
# .
#
# You have to calculate the minimum possible volume of the gas tank in your car (in liters) that will allow you to travel from the point 0
#  to the point x
#  and back to the point 0
# .
#
# Input
# The first line contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case consists of two lines:
#
# the first line contains two integers n
#  and x
#  (1≤n≤50
# ; 2≤x≤100
# );
# the second line contains n
#  integers a1,a2,…,an
#  (0<a1<a2<⋯<an<x
# ).
# Output
# For each test case, print one integer — the minimum possible volume of the gas tank in your car that will allow you to travel from the point 0
#  to the point x
#  and back.
#
# Example
# InputCopy
# 3
# 3 7
# 1 2 5
# 3 6
# 1 2 5
# 1 10
# 7
# OutputCopy
# 4
# 3
# 7
# Note
# In the first test case of the example, if the car has a gas tank of 4
#  liters, you can travel to x
#  and back as follows:
#
# travel to the point 1
# , then your car's gas tank contains 3
#  liters of fuel;
# refuel at the point 1
# , then your car's gas tank contains 4
#  liters of fuel;
# travel to the point 2
# , then your car's gas tank contains 3
#  liters of fuel;
# refuel at the point 2
# , then your car's gas tank contains 4
#  liters of fuel;
# travel to the point 5
# , then your car's gas tank contains 1
#  liter of fuel;
# refuel at the point 5
# , then your car's gas tank contains 4
#  liters of fuel;
# travel to the point 7
# , then your car's gas tank contains 2
#  liters of fuel;
# travel to the point 5
# , then your car's gas tank contains 0
#  liters of fuel;
# refuel at the point 5
# , then your car's gas tank contains 4
#  liters of fuel;
# travel to the point 2
# , then your car's gas tank contains 1
#  liter of fuel;
# refuel at the point 2
# , then your car's gas tank contains 4
#  liters of fuel;
# travel to the point 1
# , then your car's gas tank contains 3
#  liters of fuel;
# refuel at the point 1
# , then your car's gas tank contains 4
#  liters of fuel;
# travel to the point 0
# , then your car's gas tank contains 3
#  liters of fuel.
# Solution
# C++ O(N) O(1) Greedy
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, x;
        std::cin >> n >> x;
        std::vector<int> stations (n, 0);
        for (int j = 0; j < n; ++j) {
            std::cin >> stations[j];
        }
        int output = stations[0];
        bool overhead = false;
        for (int j = 1; j < n; ++j) {
            if (stations[j] > x) {
                int nextGas = output = stations[j] - stations[j - 1];
                if (j && (x - stations[j - 1]) * 2 > output) {
                    output = std::min((x - stations[j - 1]) * 2, nextGas);
                } else output = std::max(output, nextGas);
                overhead = true;
                break;
            }
            else {
                output = std::max(output, stations[j] - stations[j - 1]);
            }
        }
        if (!overhead) output = std::max(output, (x - stations[n - 1]) * 2);
        std::cout << output << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().rstrip().split())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        output: int = nums[0]
        overhead: bool = False
        for i in range(1, n):
            if nums[i] > x:
                overhead = True
                next_gas: int = nums[i] - nums[i - 1]
                if i: output = output = max(output, min(next_gas, (x - nums[j]) * 2))
                else: output = max(output, next_gas)
            else: output = max(output, nums[i] - nums[i - 1])
        if not overhead: output = max(output, (x - nums[-1]) * 2)
        sys.stdout.write(str(output) + '\n')


if __name__ == '__main__':
    solution()