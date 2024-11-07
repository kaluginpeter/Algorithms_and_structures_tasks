# Task
# Write a function that takes a string and finds a repeating character in the string (there may be multiple repeating characters). The function should return the minimum difference between the indices of these characters and the character itself.
#
# For example, in the string "aabcba", the minimum position difference of repeated characters will be equal to 1, since for the character "a", the position difference is 1.
#
# The output should be in the form of an array.
#
# If there are no duplicate characters in the string, it should return null.
#
# The string can only contain lowercase letters, and nothing else!!! (an empty string is not allowed).
#
# If the difference between repeated characters is the same, return the first character encountered.
#
# Examples of outputs:
#
# "aa" => new Object[]{1, 'a'}
#
# "aabbca" => new Object[]{1, 'a'}
#
# "abka" => new Object[]{3, 'a'}
#
# "abcded" => new Object[]{2, 'd'}
#
# "abbbbbc" => new Object[]{1, 'b'}
#
# "abc" => null
# Strings
# Solution
def min_repeating_character_difference(text):
    hashmap: dict[str, int] = dict()
    main_diff: int = float('inf')
    main_char: str = ''
    for idx in range(len(text)):
        if text[idx] in hashmap:
            if idx - hashmap[text[idx]] < main_diff:
                main_diff = idx - hashmap[text[idx]]
                main_char = text[idx]
        hashmap[text[idx]] = idx
    return (main_diff, main_char) if main_char else None