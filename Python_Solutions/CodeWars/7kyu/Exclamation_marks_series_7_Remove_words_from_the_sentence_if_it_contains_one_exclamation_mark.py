# Description:
# Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space, without leading/trailing spaces.
#
# Examples
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
# FUNDAMENTALSSTRINGSALGORITHMS
# Solution
def remove(s):
    return ' '.join(filter(lambda word: word.count('!') != 1, s.split(' ')))