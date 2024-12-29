# B. Two-gram
# time limit per test1 second
# memory limit per test256 megabytes
# Two-gram is an ordered pair (i.e. string of length two) of capital Latin letters. For example, "AZ", "AA", "ZA" — three distinct two-grams.

# You are given a string s
#  consisting of n
#  capital Latin letters. Your task is to find any two-gram contained in the given string as a substring (i.e. two consecutive characters of the string) maximal number of times. For example, for string s
#  = "BBAABBBA" the answer is two-gram "BB", which contained in s
#  three times. In other words, find any most frequent two-gram.

# Note that occurrences of the two-gram can overlap with each other.

# Input
# The first line of the input contains integer number n
#  (2≤n≤100
# ) — the length of string s
# . The second line of the input contains the string s
#  consisting of n
#  capital Latin letters.

# Output
# Print the only line containing exactly two capital Latin letters — any two-gram contained in the given string s
#  as a substring (i.e. two consecutive characters of the string) maximal number of times.

# Examples
# InputCopy
# 7
# ABACABA
# OutputCopy
# AB
# InputCopy
# 5
# ZZZAA
# OutputCopy
# ZZ
# Note
# In the first example "BA" is also valid answer.

# In the second example the only two-gram "ZZ" can be printed because it contained in the string "ZZZAA" two times.

# Solution
# C++ O(N) O(N) HashMap Greedy
#include <iostream>
#include <string>
#include <unordered_map>


void solution(int& n, std::string& sequence) {
    std::unordered_map<std::string, int> hashmap;
    for (int i = 0; i < n - 1; ++i) {
        ++hashmap[sequence.substr(i, 2)];
    }
    std::string output;
    int maxFreq = 0;
    for (auto& pair : hashmap) {
        if (pair.second > maxFreq) {
            output = pair.first;
            maxFreq = pair.second;
        }
    }
    std::cout << output << "\n";
}


int main() {
    int n;
    std::cin >> n;
    std::string sequence;
    std::cin >> sequence;
    solution(n, sequence);
}

# Python O(N) O(N) HashMap Greedy
import sys


def solution(n: int, sequence: str) -> None:
    hashmap: dict = dict()
    for i in range(n - 1):
        hashmap[sequence[i:i+2]] = hashmap.get(sequence[i:i+2], 0) + 1
    output: str = ''
    max_freq: int = 0
    for substr, freq in hashmap.items():
        if freq > max_freq:
            output = substr
            max_freq = freq
    sys.stdout.write(f'{output}\n')

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sequence: str = sys.stdin.readline().rstrip()
    solution(n, sequence)
    