# B. Books
# time limit per test2 seconds
# memory limit per test256 megabytes
# When Valera has got some free time, he goes to the library to read some books. Today he's got t free minutes to read. That's why Valera took n books in the library and for each book he estimated the time he is going to need to read it. Let's number the books by integers from 1 to n. Valera needs ai minutes to read the i-th book.
#
# Valera decided to choose an arbitrary book with number i and read the books one by one, starting from this book. In other words, he will first read book number i, then book number i + 1, then book number i + 2 and so on. He continues the process until he either runs out of the free time or finishes reading the n-th book. Valera reads each book up to the end, that is, he doesn't start reading the book if he doesn't have enough free time to finish reading it.
#
# Print the maximum number of books Valera can read.
#
# Input
# The first line contains two integers n and t (1 ≤ n ≤ 105; 1 ≤ t ≤ 109) — the number of books and the number of free minutes Valera's got. The second line contains a sequence of n integers a1, a2, ..., an (1 ≤ ai ≤ 104), where number ai shows the number of minutes that the boy needs to read the i-th book.
#
# Output
# Print a single integer — the maximum number of books Valera can read.
#
# Examples
# inputCopy
# 4 5
# 3 1 2 1
# outputCopy
# 3
# inputCopy
# 3 3
# 2 2 3
# outputCopy
# 1
# Solution Sliding Window O(N) O(1)
import sys


def solution(t: int, n: int, books: list) -> str:
    left = 0
    current_time = 0
    max_books = 0

    for right in range(t):
        current_time += books[right]
        while current_time > n:
            current_time -= books[left]
            left += 1
        max_books = max(max_books, right - left + 1)

    return str(max_books)


if __name__ == '__main__':
    t, n = map(int, sys.stdin.readline().rstrip().split())
    books: list = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(t, n, books))
