# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:
#
# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
#
# --> "alpha beta gamma delta alpha beta gamma delta"
# Words will be separated by a single space. There will be no leading or trailing spaces in the string. An empty string (0 words) is a valid input.
#
# STRINGSREGULAR EXPRESSIONSALGORITHMS
# Solution
def remove_consecutive_duplicates(s):
    if not s:
        return ''
    s= s.split()
    w = [s[0]]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            w.append(s[i])
    return ' '.join(w)