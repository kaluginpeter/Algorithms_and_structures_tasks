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
# Solution
def strings_in_max_depth(s) -> list[str]:
    output: list[tuple[int, str]] = []
    stack: list[tuple[int, str]] = []
    depth: int = 0
    cur_string: str = ''
    for i in range(len(s)):
        if s[i] == '(':
            stack.append((depth, cur_string))
            depth += 1
            cur_string = ''
        elif s[i] == ')':
            if not output or output[0][0] < depth:
                output.clear()
                output.append((depth, cur_string))
            elif output and output[0][0] == depth:
                output.append((depth, cur_string))
            cur_string = stack.pop()[1]
            depth -= 1
        else:
            cur_string += s[i]
    if not output:
        output.append((depth, cur_string))
    return [substring for depth, substring in output]