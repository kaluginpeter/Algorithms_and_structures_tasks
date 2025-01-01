# Given a balanced string with brackets like: "AA(XX((YY))(U))" find the substrings that are enclosed in the greatest depth.
#
# Example:
# String:  A   A   (   X   X   (   (   Y   Y   )   )   (   U   )   )
# Level:        1        2  3       3  2  2    2  1
#
# Therefore, answer: { "YY" } since the substring "YY" is locked at the deepest level.
# If several substring are at the deepest level, return them all in a list in order of appearance.
#
# The string includes only uppercase letters, parenthesis '(' and ')'.
# If the input is empty or doesn't contain brackets, an array containing only the original string must be returned.
#
# StringsPerformanceAlgorithms