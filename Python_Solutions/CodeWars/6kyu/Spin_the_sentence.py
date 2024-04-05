# In this kata you will have to modify a sentence so it meets the following rules:
#
# convert every word backwards that is:
#
# longer than 6 characters
# OR
#
# has 2 or more 'T' or 't' in it
# convert every word uppercase that is:
#
# exactly 2 characters long
# OR
#
# before a comma
# convert every word to a "0" that is:
#
# exactly one character long
# NOTES:
#
#   Punctuation must not be touched. if a word is 6 characters long, and a "." is behind it,
#   it counts as 6 characters so it must not be flipped, but if a word is 7 characters long,
#   it must be flipped but the "." must stay at the end of the word.
#   -----------------------------------------------------------------------------------------
#   Only the first transformation applies to a given word, for example 'companions,'
#   will be 'snoinapmoc,' and not 'SNOINAPMOC,'.
#   -----------------------------------------------------------------------------------------
#   As for special characters like apostrophes or dashes, they count as normal characters,
#   so e.g 'sand-colored' must be transformed to 'deroloc-dnas'.
# STRINGSFUNDAMENTALS
# Solution
def spin_solve(sentence):
    ans: list[str] = list()
    for word in sentence.split():
        x: str = word[:]
        end: bool = False
        while not x[-1].isalnum():
            x, end = x[:-1], True
        if len(x) > 6 or x.count('T') > 1 or x.count('t') > 1:
            ans.append(x[::-1] + (word[-1] if end else ''))
        elif len(x) == 2 or (end and word[-1] == ','):
            ans.append(x.upper() + (word[-1] if end else ''))
        elif len(x) == 1:
            ans.append('0')
        else:
            ans.append(x + (word[-1] if end else ''))
    return ' '.join(ans)