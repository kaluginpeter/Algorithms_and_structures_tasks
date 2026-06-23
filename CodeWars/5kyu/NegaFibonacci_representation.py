# Zeckendorf's Theorem[wiki] states that every positive integer can be represented uniquely as the sum of one or more distinct Fibonacci numbers in such a way that the sum does not include any two consecutive Fibonacci numbers. This representation can be used for Fibonacci Coding[wiki] of positive integers.
#
# The representation and encoding can be extended to use NegaFibonacci numbers[wiki], which would allow us to encode negative numbers as well as positive numbers. 0 Can be represented, but not encoded; this kata will therefore use the representation and not the encoding for its expected value.
#
# Task
# Define a function that accepts an integer and returns its representation as an array of zero (!) or more non-consecutive NegaFibonacci integers, sorted descending by absolute value.
#
# Examples
# negative_fibonacci_representation(0) => []
# negative_fibonacci_representation(1) => [1]
# negative_fibonacci_representation(4) => [5,-1]
# negative_fibonacci_representation(-17) => [-21,5,-1]
# negative_fibonacci_representation(64) => [89,-21,-3,-1]
# Notes
# The formula that generates the Fibonacci numbers in one direction also generates the NegaFibonacci numbers in the other direction. The first 12 terms are given in the Example tests, but you'll need more.
# This is not intended to be a performance kata, but there will be ~3000 tests over the full range of Int ( Python: abs(n) <= 2^64 ). Your naive Fibonacci implementation will bomb. :]
# I take no responsibility for the content of external resources.
# Number TheoryPuzzlesAlgorithms