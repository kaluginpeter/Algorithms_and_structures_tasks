# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
#
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false
# STRINGSFUNDAMENTALS
# Solution
def is_isogram(string):
    some_string = ''
    for word in string.lower():
        if word not in some_string:
            some_string += word
    print(some_string)
    if len(some_string) == len(string):
        return True
    else:
        return False