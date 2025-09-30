# Task
# You're given a sentence, where each word has different length. Swap the longest word with the shortest one, the 2nd shortest word with the 2nd longest one, and so on.
#
# Note that the resulting sentence should be correct, i.e. it should be capitalized and all words but the first one should contain only lowercase letters (except the word "I").
#
# Input/Output
# [input] string sentence
# A string of English letters and whitespace characters.
# 0 < sentence.length <= 20.
#
# [output] a string
# Correct sentence with words replaced. It should be capitalized and all words but the first one should contain only lowercase letters (except the word "I").
#
# Examples
# For sentence = "I am the best", the output should be "Best the am I"
#
# The word "I" and word "best" exchanged their positions; The word "am" and word "the" exchanged their positions.
#
# For sentence = "I am better than him", the output should be "Better than I am him"
#
# The word "I" and word "better" exchanged their positions; The word "am" and word "than" exchanged their positions; The middle length word "him" remain in its original position.
#
# Fundamentals
# Solution
from collections import defaultdict
def replace_words(sentence):
    words: list[str] = sentence.split()
    hashmap: dict[int, list[int]] = defaultdict(list)
    for i in range(len(words)):
        hashmap[words[i]].append(i)
    correct: list[str] = sorted(words, key=lambda word: len(word))
    while len(correct) > 1:
        left: int = hashmap[correct.pop(0)].pop(0)
        right: int = hashmap[correct.pop()].pop(0)
        words[left], words[right] = words[right], words[left]
    for i in range(len(words)):
        if not i: words[i] = words[i].title()
        elif words[i].lower() == 'i': words[i] = words[i].upper()
        else: words[i] = words[i].lower()
    return ' '.join(words)