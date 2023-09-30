# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
#
# Example:
#
# Input:
#
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#
# Output:
#
# 'alpha beta gamma delta'
#
# STRINGSREGULAR EXPRESSIONSALGORITHMS
# Solution
def remove_duplicate_words(s):
    l = []
    for word in s.split():
        if word not in l:
            l.append(word)
    return ' '.join(l)