# Given two arrays a1 and a2 of positive integers find the set of common elements between them and return the elements (a set) that have a sum or difference equal to either array length.
#
# All elements will be positive integers greater than 0
# If there are no results an empty set should be returned
# Each operation should only use two elements
# Examples
#
# a1 = [1, 2, 3, 4, 5, 6]
# a2 = [1, 2, 4, 6, 7, 8, 9, 10]
# should return {2, 4, 6} because all three integers exist in both arrays and a1 has a length of 6 (2+4) and a2 has a length of 8 (2+6).
#
# a1 = [1, 2, 3, 5, 10, 15]
# a2 = [1, 2, 3, 4, 5, 6, 10, 12, 15, 16]
# should return {1, 5, 15} because all 3 integers exist in both arrays and a1 has a length of 6 (1+5) and a2 has a length of 10 (15-5).
#
# LISTSPERMUTATIONSFUNDAMENTALS