# Write a function that determines whether the passed in sequences are similar.
# Similar means they contain the same elements, and the same number of occurrences of elements.
#
# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 1, 2, 4, 3]
# arr3 = [1, 2, 3, 4]
# arr4 = [1, 2, 3, "4"]
# arrays_similar(arr1, arr2) # Should equal true
# arrays_similar(arr2, arr3) # Should equal false
# arrays_similar(arr3, arr4) # Should equal false
# ARRAYSALGORITHMS
# Solution
def arrays_similar(seq1, seq2):
    l1 = ''.join(str(i) for i in seq1)
    l2 = ''.join(str(i) for i in seq2)
    return set(seq1) == set(seq2) and sorted(l1) == sorted(l2)