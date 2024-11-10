# Given a string which is a word, return True if the word has adjacent double double letters, like in 'balloon'.
#
# For example,
#
# 'balloon' -> True, 'lloo' are adjacent double double letters
#
# 'baaloon' -> False, because even though there are two double letters, they are not adjacent
#
# 'baboonn' -> True, here 'oonn' are adjacent double double letters
#
# 'matte'   -> False, because there is only one pair of double letters
#
# 'aaaaaaah'  -> True, any substring 'aaaa' makes it a word with adjacent double double letters
#
# Note: all the words will be lowercase, without any symbols or spaces
#
# FundamentalsStrings
# Solution
# Python O(N) O(1)
def adjacent_double_double_letters(word):
    if len(word) < 4: return False
    return any(word[idx - 3] == word[idx - 2] and word[idx - 1] == word[idx] for idx in range(3, len(word)))