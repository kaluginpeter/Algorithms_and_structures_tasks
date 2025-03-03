# A. Sakurako and Kosuke
# time limit per test1 second
# memory limit per test256 megabytes
# Sakurako and Kosuke decided to play some games with a dot on a coordinate line. The dot is currently located in position x=0
# . They will be taking turns, and Sakurako will be the one to start.
#
# On the i
# -th move, the current player will move the dot in some direction by 2⋅i−1
#  units. Sakurako will always be moving the dot in the negative direction, whereas Kosuke will always move it in the positive direction.
#
# In other words, the following will happen:
#
# Sakurako will change the position of the dot by −1
# , x=−1
#  now
# Kosuke will change the position of the dot by 3
# , x=2
#  now
# Sakurako will change the position of the dot by −5
# , x=−3
#  now
# ⋯
# They will keep on playing while the absolute value of the coordinate of the dot does not exceed n
# . More formally, the game continues while −n≤x≤n
# . It can be proven that the game will always end.
#
# Your task is to determine who will be the one who makes the last turn.
#
# Input
# The first line contains one integer t
#  (1≤t≤100
# ) — the number of games that Sakurako and Kosuke played.
#
# Each game is described by one number n
#  (1≤n≤100
# ) — the number that defines the condition when the game ends.
#
# Output
# For each of the t
#  games, output a line with the result of that game. If Sakurako makes the last turn, output "Sakurako" (without quotes); else output "Kosuke".
#
# Example
# InputCopy
# 4
# 1
# 6
# 3
# 98
# OutputCopy
# Kosuke
# Sakurako
# Kosuke
# Sakurako
# Solution
# C++ O(logN) O(1) Simulation
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        bool isFirst = false;
        int bound = 0;
        int move = 1;
        while (bound <= n && bound >= -n) {
            isFirst = !isFirst;
            if (isFirst) bound += -(2 * move - 1);
            else bound += 2 * move - 1;
            ++move;
        }
        std::cout << (isFirst? "Sakurako" : "Kosuke") << "\n";
    }
}


int main() {
    solution();
}

# Python O(logN) O(1) Simulation
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        bound: int = 0
        move: int = 1
        is_first: bool = False
        while -n <= bound <= n:
            is_first = not is_first
            if is_first: bound += -(2 * move - 1)
            else: bound += 2 * move - 1
            move += 1
        sys.stdout.write(['Kosuke', 'Sakurako'][is_first] + '\n')


if __name__ == '__main__':
    solution()