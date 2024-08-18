# Write a function that returns the count of characters that have
# to be removed in order to get a string with no consecutive repeats.
#
# Note: This includes any characters
#
# Examples
# 'abbbbc'  => 'abc'    #  answer: 3
# 'abbcca'  => 'abca'   #  answer: 2
# 'ab cca'  => 'ab ca'  #  answer: 1
# STRINGSFUNDAMENTALS
# Solution
def count_repeats(txt):
    return sum(1 if i == j else 0 for i, j in zip(txt, txt[1:]))