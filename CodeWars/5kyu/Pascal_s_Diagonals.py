# Create a function that returns an array containing the first l numbers from the nth diagonal of Pascal's triangle.
#
# n = 0 should generate the first diagonal of the triangle (the ones).
# The first number in each diagonal should be 1.
# If l = 0, return an empty array.
# Both n and l will be non-negative integers in all test cases.
#
# Algorithms
# Solution
def generate_diagonal(n, l):
    if l == 0: return []

    output: list[int] = [1]
    for k in range(1, l):
        output.append(output[-1] * (n + k) // k)
    return output