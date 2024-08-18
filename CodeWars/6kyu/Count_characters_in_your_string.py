# The main idea is to count all the occurring characters in a string. If you have a string like aba,
# then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.
#
# STRINGSFUNDAMENTALS
# Solution
def count(string):
    dict = {}
    count = 0
    for char in string:
        count = string.count(char)
        dict[f"{char}"] = count
    return dict