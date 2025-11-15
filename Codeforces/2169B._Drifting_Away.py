# B. Drifting Away
# time limit per test2 seconds
# memory limit per test512 megabytes
# There's a river flowing in front of Monocarp's house, which can be represented as a strip of cells. In some cells, there is a strong current, while in others, there is no current. It can be represented as a string s
# , consisting of the following characters:
#
# the "less-than" sign ('<') — leftward current;
# the "greater-than" sign ('>') — rightward current;
# an asterisk ('*') — no current.
# At first, Monocarp chooses the cell to start his journey along the river at.
#
# If there is a current in the cell, where Monocarp is at the moment, he is carried to the neighboring cell in the direction of the current. If there is no neighboring cell (i. e., a leftward current in cell 1
#  or a rightward current in cell n
# ), Monocarp ends up on the shore. Each move takes one minute.
#
# If there is no current in the cell, where Monocarp is at the moment, he rows to the neighboring cell on the left or to the neighboring cell on the right. If there is no neighboring cell in the direction where Monocarp decides to row to, he ends up on the shore. Each move also takes one minute.
#
# Monocarp wants to sail along the river for as long as possible. If Monocarp can sail infinitely, print −1
# . Otherwise, print the maximum time Monocarp can sail along the river before ending up on the shore.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The only line of each test case contains a string s
#  (1≤|s|≤3⋅105
# ), consisting only of characters '<' (leftward current), '>' (rightward current), '*' (no current). The ASCII codes are 60
# , 62
# , and 42
# , respectively.
#
# An additional constraint on the input: the total length of strings s
#  over all test cases does not exceed 3⋅105
# .
#
# Output
# For each test case, output a single integer:
#
# −1
# , if Monocarp can sail along the river infinitely;
# the maximum time Monocarp can sail along the river before ending up on the shore, otherwise.
# Example
# InputCopy
# 4
# *****
# <<<>
# >*<
# *
# OutputCopy
# -1
# 3
# -1
# 1