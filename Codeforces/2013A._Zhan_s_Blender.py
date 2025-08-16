# A. Zhan's Blender
# time limit per test1 second
# memory limit per test256 megabytes
# Today, a club fair was held at "NSPhM". In order to advertise his pastry club, Zhan decided to demonstrate the power of his blender.
#
# To demonstrate the power of his blender, Zhan has n
#  fruits.
#
# The blender can mix up to x
#  fruits per second.
#
# In each second, Zhan can put up to y
#  fruits into the blender. After that, the blender will blend min(x,c)
#  fruits, where c
#  is the number of fruits inside the blender. After blending, blended fruits are removed from the blender.
#
# Help Zhan determine the minimum amount of time required for Zhan to blend all fruits.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The first line of each test case contains one integer n
#  (0≤n≤109
# ) — the number of fruits Zhan has.
#
# The second line of each test case contains two integers x
#  and y
#  (1≤x,y≤109
# ) — the number of fruits the blender can blend per second and the number of fruits Zhan can put into the blender per second.
#
# Output
# For each testcase, output a single integer — the minimum number of seconds to blend all fruits.
#
# Example
# InputCopy
# 5
# 5
# 3 4
# 3
# 1 2
# 6
# 4 3
# 100
# 4 3
# 9
# 3 3
# OutputCopy
# 2
# 3
# 2
# 34
# 3
# Note
# In the first example, you can first put 2
#  fruits in the blender. After that, the blender will mix these 2
#  fruits, and in the end, there will be 0
#  fruits left in the blender. Then you can put 3
#  fruits into the blender, after which the blender will mix these 3
#  fruits.
#
# In the second example, you can put 1
#  fruit into the blender 3
#  times.
#
# In the third example, you can first put 3
#  fruits into the blender, then add another 3
#  fruits.
# C++ O(1) O(1) Math
#include <iostream>
#include <cmath>


void solution() {
    int n, x, y;
    std::cin >> n >> x >> y;
    int count = n / y + (n % y ? 1 : 0);
    if (x >= y) {
        std::cout << count << std::endl;
        return;
    }
    int output = count * y - std::abs(n - count * y);
    std::cout << output / x + (output % x ? 1 : 0) << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().rstrip().split())
    count: int = n // y + int(bool(n % y))
    if x >= y:
        sys.stdout.write('{}\n'.format(count))
        return
    output: int = count * y - abs(count * y - n)
    sys.stdout.write('{}\n'.format(output // x + int(bool(output % x))))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()