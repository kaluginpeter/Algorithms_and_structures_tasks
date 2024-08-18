# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.
#
# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
#
# As a simplification, you may assume that no letter occurs more than once in the secret string.
#
# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
#
# ALGORITHMS
# Solution
def recoverSecret(triplets):
    unique_letters = set()
    letter_order = {}
    for triplet in triplets:
        for letter in triplet:
            unique_letters.add(letter)
    for triplet in triplets:
        for i in range(2):
            if triplet[i + 1] not in letter_order:
                letter_order[triplet[i + 1]] = set()
            letter_order[triplet[i + 1]].add(triplet[i])
    sorted_letters = []
    while unique_letters:
        for letter in unique_letters:
            if letter not in letter_order or not letter_order[letter]:
                sorted_letters.append(letter)
                unique_letters.remove(letter)
                for key in letter_order:
                    if letter in letter_order[key]:
                        letter_order[key].remove(letter)
                break
    return ''.join(sorted_letters)