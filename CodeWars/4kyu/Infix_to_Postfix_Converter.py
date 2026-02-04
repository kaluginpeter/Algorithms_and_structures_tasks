# Construct a function that, when given a string containing an expression in infix notation, will return an identical expression in postfix notation.
#
# The operators used will be +, -, *, /, and ^ with left-associativity of all operators but ^.
#
# The precedence of the operators (most important to least) are : 1) parentheses, 2) exponentiation, 3) times/divide, 4) plus/minus.
#
# The operands will be single-digit integers between 0 and 9, inclusive.
#
# Parentheses may be included in the input, and are guaranteed to be in correct pairs.
#
# to_postfix("2+7*5") # Should return "275*+"
# to_postfix("3*3/(7+1)") # Should return "33*71+/"
# to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
# to_postfix("1^2^3") # Should return "123^^"
# You may read more about postfix notation, also called Reverse Polish notation, here: http://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# MathematicsAlgorithms
# Solution
def to_postfix(infix):
    output = []
    ops = []

    def precedence(op):
        if op == '^': return 3
        if op in '*/': return 2
        if op in '+-': return 1
        return 0

    def is_right_associative(op):
        return op == '^'

    def is_operator(c):
        return c in '+-*/^'
    for c in infix:
        if c.isdigit(): output.append(c)
        elif c == '(': ops.append(c)
        elif c == ')':
            while ops and ops[-1] != '(': output.append(ops.pop())
            ops.pop()
        elif is_operator(c):
            while (
                ops and is_operator(ops[-1]) and
                (
                    precedence(ops[-1]) > precedence(c) or
                    (
                        precedence(ops[-1]) == precedence(c)
                        and not is_right_associative(c)
                    )
                )
            ):
                output.append(ops.pop())
            ops.append(c)
    while ops: output.append(ops.pop())
    return ''.join(output)