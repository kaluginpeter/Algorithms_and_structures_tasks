# Task
# Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.
#
# Examples
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi Hi"
# remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"
# STRINGSREGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def remove(s):
    l = []
    for i in s.split():
        while i.endswith('!'):
            i = i[:-1]
        l.append(i)
    return ' '.join(l)