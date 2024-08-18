# Hofstadter sequences are a family of related integer sequences, among which the first ones were described by an American professor Douglas Hofstadter in his book Gödel, Escher, Bach.
#
# Task
# Today we will be implementing the rather chaotic recursive sequence of integers called Hofstadter Q.
#
# The Hofstadter Q is defined as:
#
#
# As the author states in the aforementioned book:
#
#
# It is reminiscent of the Fibonacci definition in that each new value is a sum of two previous values-but not of the immediately previous two values. Instead, the two immediately previous values tell how far to count back to obtain the numbers to be added to make the new value.
# The function produces the starting sequence:
# 1, 1, 2, 3, 3, 4, 5, 5, 6 . . .
# Test info: 100 random tests, n is always positive
#
# Good luck!
# RECURSIONALGORITHMS
# Solution
def hofstadter_q(n):
    if n < 3:
        return 1
    q_values = [1, 1] + [0] * (n - 2)
    for i in range(2, n):
        q_values[i] = q_values[i - q_values[i - 1]] + q_values[i - q_values[i - 2]]
    return q_values[n - 1]