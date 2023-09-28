# Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.
#
# Indices in sequence start from 0.
#
# If the sequence is empty, you should return 0.
#
# ARRAYSFUNDAMENTALS
# Solution
def even_last(numbers):
    total = 0
    if numbers:
        last = numbers[-1]
        numbers = [num for i, num in enumerate(numbers) if i % 2 ==0]
        total = sum(numbers) * last
    return total