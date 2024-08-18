# Your task is very simple. Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.
#
# For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].
#
# Goodluck :)
#
# Have a look at my other katas!
#
# Alphabetically ordered
#
# Find Nearest square number
#
# Not prime numbers
#
# Find your caterer
#
# STRINGSFUNDAMENTALS
# Solution
def case_sensitive(s):
    flag: bool = True
    ans: list = list()
    for i in s:
        if i.isupper():
            flag = not flag
            ans += i
    return [flag, ans]