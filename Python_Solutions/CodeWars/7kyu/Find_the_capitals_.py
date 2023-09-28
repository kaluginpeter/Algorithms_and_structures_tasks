# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
#
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]
# STRINGSARRAYSFUNDAMENTALS
# Solution
def capitals(word):
    return [value for value, i in enumerate(word) if i.isupper()]