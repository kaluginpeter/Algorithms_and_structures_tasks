# In this kata, your goal is to write a function which will reverse the vowels in a string.
# Any characters which are not vowels should remain in their original position. Here are some examples:
#
# "Hello!" => "Holle!"
# "Tomatoes" => "Temotaos"
# "Reverse Vowels In A String" => "RivArsI Vewols en e Streng"
# For simplicity, you can treat the letter y as a consonant, not a vowel.
#
# Good luck!
#
# STRINGSFUNDAMENTALS
# Solution
def reverse_vowels(s):
    vowels = [i for i in s if i in 'aeouiAEOIU']
    return ''.join(i if i not in 'aeoiuAEOIU' else vowels.pop() for i in s)