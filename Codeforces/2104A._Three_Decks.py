# A. Three Decks
# time limit per test2 seconds
# memory limit per test512 megabytes
# Monocarp placed three decks of cards in a row on the table. The first deck consists of a
#  cards, the second deck consists of b
#  cards, and the third deck consists of c
#  cards, with the condition a<b<c
# .
#
# Monocarp wants to take some number of cards (at least one, but no more than c
# ) from the third deck and distribute them between the first two decks so that each of the taken cards ends up in either the first or the second deck. It is possible that all the cards taken from the third deck will go into the same deck.
#
# Your task is to determine whether Monocarp can make the number of cards in all three decks equal using the described operation.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The only line of each test case contains three integers a,b
# , and c
#  (1≤a,b,c≤108
# ) — the number of cards in the first, second, and third decks, respectively.
#
# Additional constraint on the input: a<b<c
# .
#
# Output
# For each test case, output "YES" (without quotes) if Monocarp can make the number of cards in all three decks equal using the described operation. Otherwise, output "NO" (without quotes).
#
# Example
# InputCopy
# 4
# 3 5 10
# 12 20 30
# 3 5 7
# 1 5 6
# OutputCopy
# YES
# NO
# YES
# NO
# Note
# In the first test case, Monocarp has to take 4
#  cards from the third deck, put 3
#  cards in the first deck, and 1
#  card in the second deck. Thus, there will be 6
#  cards in all three decks.
#
# In the second test case, it is impossible to make the number of cards in all three decks equal.
#
# In the third test case, Monocarp has to take 2
#  cards from the third deck and put both in the first deck. Thus, there will be 5
#  cards in all three decks.
#
# In the fourth test case, it is also impossible to make the number of cards in all three decks equal.
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int a, b, c;
        std::cin >> a >> b >> c;
        if (a >= b || b >= c) {
            std::cout << "NO'\n";
            continue;
        }
        std::cout << ((c - (b - a) - b) % 3 == 0 && (c - (b - a) - b >= 0)? "YES" : "NO") << "\n";
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        if a >= b or b >= c:
            sys.stdout.write('NO\n')
            continue
        sys.stdout.write('{}\n'.format(['NO', 'YES'][(c - (b - a) - b) % 3 == 0 and (c - (b - a) - b) >= 0]))


if __name__ == '__main__':
    solution()