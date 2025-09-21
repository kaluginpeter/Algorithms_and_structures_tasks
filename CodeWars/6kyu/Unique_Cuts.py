# Task
# The function is given a string with lower-case characters. Split the string into as many substrings as possible such that each character appears in only one substring. Return the list of lengths of the resulting substrings.
#
# Examples
# "abbccc" ➞ [1, 2, 3]
# # "a", "bb", "ccc"
#
# "abbacdceef" ➞ [4, 3, 2, 1]
# # "abba", "cdc", "ee", "f"
#
# "abacded" ➞ [3, 1, 3]
# # "aba", "c", "ded"
#
# "abcdea" ➞ [6]
# # "abcdea" because first letter is equal to the last letter.
# Solution
def split_string(st):
    in_: list[int] = [-1] * 26
    out_: list[int] = [-1] * 26
    for i in range(len(st)):
        j: int = ord(st[i]) - 97
        if in_[j] == -1: in_[j] = i
        out_[j] = i
    output: list[int] = []
    left: int = 0
    end: int = 0
    for right in range(len(st)):
        idx: int = ord(st[right]) - 97
        if right > end:
            output.append(end - left + 1)
            left = right
        end = max(end, out_[idx])
    output.append(len(st) - left)
    return output