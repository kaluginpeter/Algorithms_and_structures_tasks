# Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.
#
# flatten [1,2,3] # => [1,2,3]
# flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
# flatten [[[1,2,3]]] # => [[1,2,3]]
# FUNCTIONAL PROGRAMMINGARRAYSFUNDAMENTALS
# Solution
def flatten(lst):
    return sum(([i] if not isinstance(i, list) else i for i in lst), [])