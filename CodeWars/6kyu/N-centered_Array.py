# An array is called centered-N if some consecutive sequence of elements of the array sum to N and this sequence is preceded and followed by the same number of elements.
#
# Example:
#
# [3,2,10,4,1,6,9] is centered-15
# because the sequence 10,4,1 sums to 15 and the sequence
# is preceded by two elements [3,2] and followed by two elements [6,9]
# Write a method called isCenteredN that returns :
#
# true if its array argument is not empty and centered-N or empty and centered-0
# otherwise returns false.
# Fundamentals
# Solution
def is_centered(xs: list[int], n: int) -> bool:
    if not xs: return False
    left: int = 0
    right: int = len(xs) - 1
    acc: int = sum(xs)
    while left <= right:
        if acc == n: return True
        acc -= xs[left]
        acc -= xs[right]
        left += 1
        right -= 1
    return acc == n and not (len(xs) & 1)