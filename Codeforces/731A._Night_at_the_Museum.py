# A. Night at the Museum
# time limit per test1 second
# memory limit per test256 megabytes
# Grigoriy, like the hero of one famous comedy film, found a job as a night security guard at the museum. At first night he received embosser and was to take stock of the whole exposition.
#
# Embosser is a special devise that allows to "print" the text of a plastic tape. Text is printed sequentially, character by character. The device consists of a wheel with a lowercase English letters written in a circle, static pointer to the current letter and a button that print the chosen letter. At one move it's allowed to rotate the alphabetic wheel one step clockwise or counterclockwise. Initially, static pointer points to letter 'a'. Other letters are located as shown on the picture:
#
#
# After Grigoriy add new item to the base he has to print its name on the plastic tape and attach it to the corresponding exhibit. It's not required to return the wheel to its initial position with pointer on the letter 'a'.
#
# Our hero is afraid that some exhibits may become alive and start to attack him, so he wants to print the names as fast as possible. Help him, for the given string find the minimum number of rotations of the wheel required to print it.
#
# Input
# The only line of input contains the name of some exhibit — the non-empty string consisting of no more than 100 characters. It's guaranteed that the string consists of only lowercase English letters.
#
# Output
# Print one integer — the minimum number of rotations of the wheel, required to print the name given in the input.
#
# Examples
# InputCopy
# zeus
# OutputCopy
# 18
# InputCopy
# map
# OutputCopy
# 35
# InputCopy
# ares
# OutputCopy
# 34
# Note
#
#
#
# To print the string from the first sample it would be optimal to perform the following sequence of rotations:
#
# from 'a' to 'z' (1 rotation counterclockwise),
# from 'z' to 'e' (5 clockwise rotations),
# from 'e' to 'u' (10 rotations counterclockwise),
# from 'u' to 's' (2 counterclockwise rotations).
# In total, 1 + 5 + 10 + 2 = 18 rotations are required.
# Solution
# C++ O(N) O(1) Math Greedy String
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cin >> name;
    int moves = 0;
    char curChar = 'a';
    for (char letter : name) {
        int curPos = curChar - 'a' + 1;
        int nextPos = letter - 'a' + 1;
        if (nextPos >= curPos) {
            moves += std::min(nextPos - curPos, 26 - nextPos + curPos);
        } else {
            moves += std::min(curPos - nextPos, 26 - curPos + nextPos);
        }
        curChar = letter;
    }
    std::cout << moves << std::endl;
}

# Python O(N) O(1) Math Greedy String
import sys


def solution(name: str) -> int:
    cur_char: str = 'a'
    moves: int = 0
    for letter in name:
        cur_pos: int = ord(cur_char) - 96
        next_pos: int = ord(letter) - 96
        if next_pos >= cur_pos:
            moves += min(next_pos - cur_pos, 26 - next_pos + cur_pos)
        else:
            moves += min(cur_pos - next_pos, 26 - cur_pos + next_pos)
        cur_char = letter
    return moves


if __name__ == '__main__':
    name: str = sys.stdin.readline().rstrip()
    sys.stdout.write(str(solution(name)))
