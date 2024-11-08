# A. Keyboard
# time limit per test2 seconds
# memory limit per test256 megabytes
# Our good friend Mole is trying to code a big message. He is typing on an unusual keyboard with characters arranged in following way:
#
#
# qwertyuiop
# asdfghjkl;
# zxcvbnm,./
# Unfortunately Mole is blind, so sometimes it is problem for him to put his hands accurately. He accidentally moved both his hands with one position to the left or to the right. That means that now he presses not a button he wants, but one neighboring button (left or right, as specified in input).
#
# We have a sequence of characters he has typed and we want to find the original message.
#
# Input
# First line of the input contains one letter describing direction of shifting ('L' or 'R' respectively for left or right).
#
# Second line contains a sequence of characters written by Mole. The size of this sequence will be no more than 100. Sequence contains only symbols that appear on Mole's keyboard. It doesn't contain spaces as there is no space on Mole's keyboard.
#
# It is guaranteed that even though Mole hands are moved, he is still pressing buttons on keyboard and not hitting outside it.
#
# Output
# Print a line that contains the original message.
#
# Examples
# InputCopy
# R
# s;;upimrrfod;pbr
# OutputCopy
# allyouneedislove
# Solution
# C++ O(N) O(1) String
#include <iostream>
#include <string>

int main() {
    char shift;
    std::cin >> shift;
    std::string typing;
    std::cin >> typing;
    std::string alphabet = "qwertyuiopasdfghjkl;zxcvbnm,./";
    for (char typ : typing) {
        int index = 0;
        while (alphabet[index] != typ) {
            ++index;
        }
        std::cout << (shift == 'R'? alphabet[index - 1] : alphabet[index + 1]);
    }
}

# Python O(N) O(1) String
import sys


def solution() -> None:
    alpha: str = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    shift: str = sys.stdin.readline().rstrip()
    text: str = sys.stdin.readline().rstrip()
    for letter in text:
        idx: int = 0
        while alpha[idx] != letter:
            idx += 1
        sys.stdout.write(alpha[idx + (-1 if shift == 'R' else 1)])


if __name__ == '__main__':
    solution()
