# A. Alice and Books
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Alice has n
#  books. The 1
# -st book contains a1
#  pages, the 2
# -nd book contains a2
#  pages, …
# , the n
# -th book contains an
#  pages. Alice does the following:
#
# She divides all the books into two non-empty piles. Thus, each book ends up in exactly one of the two piles.
# Alice reads one book with the highest number in each pile.
# Alice loves reading very much. Help her find the maximum total number of pages she can read by dividing the books into two piles.
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤500
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the number of books Alice has.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the number of pages in each book.
#
# Output
# For each test case, output a single integer — the maximum number of pages Alice can read.
#
# Example
# inputCopy
# 5
# 2
# 1 1
# 4
# 2 3 3 1
# 5
# 2 2 3 2 2
# 2
# 10 3
# 3
# 1 2 3
# outputCopy
# 2
# 4
# 5
# 13
# 5
# Note
# In the first test case, Alice can put book number 1
#  in the first pile, and book number 2
#  in the second pile. Then she will read a1+a2=1+1=2
#  pages.
#
# In the second test case, Alice can put books with numbers 2
#  and 3
#  in the first pile, and books with numbers 1
#  and 4
#  in the second pile. Then she will read the book with the highest number 3
#  from the first pile, and the book with the highest number 4
#  from the second pile. Then she will read a3+a4=3+1=4
#  pages.