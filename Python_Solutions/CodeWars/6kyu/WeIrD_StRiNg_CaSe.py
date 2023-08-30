# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.
#
# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
#
# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
# STRINGSALGORITHMS
# Solution
def to_weird_case(words):
    words, ans = words.split(), []
    for i in words:
        top = ''
        for j in range(len(i)):
            if j % 2 == 0:
                top += i[j].upper()
            else:
                top += i[j].lower()
        ans.append(top)
    return ' '.join(ans)