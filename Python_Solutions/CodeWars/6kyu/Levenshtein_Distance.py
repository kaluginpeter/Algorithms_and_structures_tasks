# In information theory and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one word into the other.
#
# (http://en.wikipedia.org/wiki/Levenshtein_distance)
#
# Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.
#
# STRINGSALGORITHMS
# Solution
def levenshtein(a,b):
    cost: int = sum(x != y for x, y in zip(a, b))
    if len(a) == len(b): return cost
    up: int = max(len(a), len(b))
    do: int = min(len(a), len(b))
    big: str = a if len(a) == up else b
    small: str = a if len(a) == do else b
    for i in range(up):
        if up - i < do: break
        cost = min(cost, sum(x != y for x, y in zip(big[i:], small)))
    return cost + (up - do)