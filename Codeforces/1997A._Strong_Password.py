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