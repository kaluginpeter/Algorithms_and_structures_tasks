# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:
#
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:
#
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
# More examples in test cases. Good luck!
#
# Please also try:
#
# Simple time difference
#
# Simple remove duplicates
#
# FUNDAMENTALS
# Solution
def solve(s):
    count_lower: int = 0
    count_upper: int = 0
    for i in s:
        if i.islower():
            count_lower += 1
            continue
        count_upper += 1
    if count_lower >= count_upper:
        return s.lower()
    return s.upper()