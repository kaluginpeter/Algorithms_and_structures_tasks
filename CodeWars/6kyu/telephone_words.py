# Businesses use keypad letters in creative ways to spell out a phone number and make it more memorable. Example: http://en.wikipedia.org/wiki/File:Telephone-keypad2.svg
#
# Create a mapping for your dialer as given in the above link. Constraints:
#
# letters are all uppercase
# digits 0, 1 are mapped to 0, 1 respectively
# Write a function that takes four digits of a phone number, and returns a list of all of the words that can be written with that number. (You should return all permutations, not only English words.)
#
# STRINGSARRAYSALGORITHMS
# Solution
def telephone_words(digit_string):
    letters: list = [['0'], ['1'], ['ABC'], ['DEF'], ['GHI'],
                    ['JKL'], ['MNO'], ['PQRS'], ['TUV'], ['WXYZ']]
    ans: list = []
    for first in letters[int(digit_string[0])][0]:
        for second in letters[int(digit_string[1])][0]:
            for third in letters[int(digit_string[2])][0]:
                for fourth in letters[int(digit_string[3])][0]:
                    ans.append(first + second + third + fourth)
    return ans