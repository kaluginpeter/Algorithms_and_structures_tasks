# A. QAQ
# time limit per test1 second
# memory limit per test256 megabytes
# "QAQ" is a word to denote an expression of crying. Imagine "Q" as eyes with tears and "A" as a mouth.
#
# Now Diamond has given Bort a string consisting of only uppercase English letters of length n. There is a great number of "QAQ" in the string (Diamond is so cute!).
#
# illustration by 猫屋 https://twitter.com/nekoyaliu
# Bort wants to know how many subsequences "QAQ" are in the string Diamond has given. Note that the letters "QAQ" don't have to be consecutive, but the order of letters should be exact.
#
# Input
# The only line contains a string of length n (1 ≤ n ≤ 100). It's guaranteed that the string only contains uppercase English letters.
#
# Output
# Print a single integer — the number of subsequences "QAQ" in the string.
#
# Examples
# InputCopy
# QAQAQYSYIOIWIN
# OutputCopy
# 4
# InputCopy
# QAQQQZZYNOIWIN
# OutputCopy
# 3
# Note
# In the first example there are 4 subsequences "QAQ": "QAQAQYSYIOIWIN", "QAQAQYSYIOIWIN", "QAQAQYSYIOIWIN", "QAQAQYSYIOIWIN".
# Solution
# C++ O(N) O(1) Combinatorial Dynamic Programming
#include <iostream>
#include <string>


void solution() {
    std::string sequence;
    std::cin >> sequence;
    int output = 0;
    int x = 0;
    int prev = 0;
    for (int right = 0; right < sequence.size(); ++right) {
        if (sequence[right] == 'A') prev += x;
        else if (sequence[right] == 'Q') ++x;
        if (sequence[right] == 'Q') output += prev;
    }
    std::printf("%d\n", output);
}


int main() {
    solution();
}

# Python O(N) O(1) Combinatorial DynamicProgramming
import sys


def solution() -> None:
    sequence: str = sys.stdin.readline().rstrip()
    prev: int = 0
    x: int = 0
    output: int = 0
    for right in range(len(sequence)):
        if sequence[right] == 'A': prev += x
        elif sequence[right] == 'Q':
            output += prev
            x += 1
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()