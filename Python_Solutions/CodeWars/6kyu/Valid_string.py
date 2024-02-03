# You are given a sequence of valid words and a string. Test if the string is made up by one or more words from the array.
#
# Task
# Test if the string can be entirely formed by consecutively concatenating words of the dictionary.
#
# For example:
#
# dictionary: ["code", "wars"]
#
# s1:         "codewars" =>  true  -> match 'code', 'wars'
# s2:         "codewar"  =>  false -> match 'code', unmatched 'war'
# One word from the dictionary can be used several times.
#
# STRINGSALGORITHMS
# Solution
def valid_word(seq, word):
    matches: list = []
    for i in seq:
        if word.startswith(i):
            matches.append(i)
            if matches[-1] == word:
                return True
    count: int = 0
    while True:
        top: list = []
        flag: bool = False
        for char in matches:
            for wrd in seq:
                if word.startswith(char + wrd):
                    top.append(char + wrd)
                    flag = not flag
                    if top[-1] == word:
                        return True
        matches = top
        if not flag:
            count += 1
        else:
            count = 0
        if count == 10:
            return False