# Sort the given array of strings in alphabetical order, case insensitive. For example:
#
# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]
# ARRAYSSORTING
# Solution
def sortme(words):
    return sorted(words, key=lambda x: x.lower())