# Your job is to fix the parentheses so that all opening and closing parentheses (brackets) have matching counterparts. You will do this by appending parenthesis to the beginning or end of the string. The result should be of minimum length. Don't add unnecessary parenthesis.
#
# The input will be a string of varying length, only containing '(' and/or ')'.
#
# For example:
#
# Input: ")("
# Output: "()()"
#
# Input: "))))(()("
# Output: "(((())))(()())"
# Enjoy!
#
# Refactoring
# Solution
def fix_parentheses(strng):
    stack: list[str] = []
    opens: int = 0
    closed: int = 0
    for brace in strng:
        if brace == '(':
            stack.append(brace)
            opens += 1
        else:
            if not opens:
                closed += 1
            else:
                opens -= 1
            stack.append(brace)
    return ''.join(['('] * closed + stack + [')'] * opens)