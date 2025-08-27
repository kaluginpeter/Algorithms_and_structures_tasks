# A. Strong Password
# time limit per test2 seconds
# memory limit per test512 megabytes
# Monocarp's current password on Codeforces is a string s
# , consisting of lowercase Latin letters. Monocarp thinks that his current password is too weak, so he wants to insert exactly one lowercase Latin letter into the password to make it stronger. Monocarp can choose any letter and insert it anywhere, even before the first character or after the last character.
#
# Monocarp thinks that the password's strength is proportional to the time it takes him to type the password. The time it takes to type the password is calculated as follows:
#
# the time to type the first character is 2
#  seconds;
# for each character other than the first, the time it takes to type it is 1
#  second if it is the same as the previous character, or 2
#  seconds otherwise.
# For example, the time it takes to type the password abacaba is 14
# ; the time it takes to type the password a is 2
# ; the time it takes to type the password aaabacc is 11
# .
#
# You have to help Monocarp — insert a lowercase Latin letter into his password so that the resulting password takes the maximum possible amount of time to type.
#
# Input
# The first line contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case consists of one line containing the string s
#  (1≤|s|≤10
# ), consisting of lowercase Latin letters.
#
# Output
# For each test case, print one line containing the new password — a string which can be obtained from s
#  by inserting one lowercase Latin letter. The string you print should have the maximum possible required time to type it. If there are multiple answers, print any of them.
#
# Example
# InputCopy
# 4
# a
# aaa
# abb
# password
# OutputCopy
# wa
# aada
# abcb
# pastsword
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    std::string password;
    std::cin >> password;
    bool isDouble = false;
    size_t pos = 0;
    for (size_t i = 0; i < password.size() - 1; ++i) {
        if (password[i] == password[i + 1]) {
            isDouble = true;
            pos = i;
            break;
        }
    }
    if (isDouble) {
        for (size_t i = 0; i <= pos; ++i) std::cout << password[i];
        for (int i = 0; i < 26; ++i) {
            if (i != password[pos] - 'a' && i != password[pos + 1] - 'a') {
                std::cout << static_cast<char>(i + 97);
                break;
            }
        }
        for (size_t i = pos + 1; i < password.size(); ++i) std::cout << password[i];
        std::cout << std::endl;
        return;
    }
    std::cout << static_cast<char>((password[0] - 'a' + 1) % 26 + 97) << password << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) String
import sys


def solution() -> None:
    password: str = sys.stdin.readline().rstrip()
    is_double: bool = False
    pos: int = 0
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            is_double = True
            pos = i
            break
    if is_double:
        sys.stdout.write(''.join(password[:pos + 1]))
        for i in range(26):
            if i != ord(password[pos]) - 97 and i != ord(password[pos + 1]) - 97:
                sys.stdout.write(chr(i + 97))
                break
        sys.stdout.write('{}\n'.format(''.join(password[pos + 1:])))
        return
    sys.stdout.write(chr((ord(password[0]) - 97 + 1) % 26 + 97))
    sys.stdout.write('{}\n'.format(password))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()