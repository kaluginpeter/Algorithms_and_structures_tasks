# Task
# You are given a string s. Your task is to count the number of each letter (A-Z), and make a vertical histogram as result. Look at the following examples to understand the rules.
#
# Example
# For s = "XXY YY ZZZ123ZZZ AAA BB C", the output should be:
#
#           *
#           *
#           *
# *       * *
# * *   * * *
# * * * * * *
# A B C X Y Z
# Rules
# You just need to count the uppercase letters. Any other character will be ignored.
# Using * to represent the number of characters.
# The order of output is form A to Z. Characters that do not appear in the string are ignored.
# To beautify the histogram, there is a space between every pair of columns.
# There are no extra spaces at the end of each row. Also, use "\n" to separate rows.
# Happy Coding ^_^
# FundamentalsData Visualization
# Solution
from collections import Counter

def vertical_histogram_of(s: str) -> str:
    cnt = Counter(c for c in s if 'A' <= c <= 'Z')

    letters = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if cnt[c] > 0]
    if not letters: return ""

    h = max(cnt[c] for c in letters)
    rows = []

    for level in range(h, 0, -1):
        row = ["*" if cnt[c] >= level else " " for c in letters]
        rows.append(" ".join(row).rstrip())

    rows.append(" ".join(letters))
    return "\n".join(rows)