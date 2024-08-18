# Calculate the number of items in a vector that appear at the same index in each vector, with the same value.
#
#    vector_affinity([1, 2, 3, 4, 5], [1, 2, 2, 4, 3]) # => 0.6
#    vector_affinity([1, 2, 3], [1, 2, 3]) # => 1.0
# Affinity value should be realized on a scale of 0.0 to 1.0, with 1.0 being absolutely identical. Two identical sets should always be evaulated as having an affinity or 1.0.
#
# Hint: The last example test case holds a significant clue to calculating the affinity correctly.
#
# DATA STRUCTURESALGORITHMS
# Solution
def vector_affinity(a, b):
    score: int = sum(a[idx] == b[idx] for idx in range(min(len(a), len(b))))
    module: int = max(len(a), len(b))
    return score / module if module != 0 else [0.0, 1.0][len(a) == len(b)]