# In Scala, an underscore may be used to create a partially applied version of an infix operator using placeholder syntax. For example, (_ * 3) is a function that multiplies its input by 3. With a bit of manipulation, this idea can be extended to work on any arbitrary expression.
#
# Create an value/object named x that acts as a placeholder in an arithmetic expression. The placeholder should support the four basic integer arithmetic operations: addition, subtraction, multiplication, and integral (floor) division. When the expression with placeholders is called, it should fill the placeholders in the expression from left to right (regardless of operator precedence) with the values it is given.
#
# Here are a few examples:
#
# calling (x + 3)       with [1]   gives 1 + 3               = 4
# calling (10 - x)      with [4]   gives 10 - 4              = 6
# calling (x + 2 * x)   with [1 3] gives 1 + 2 * 3   = 1 + 6 = 7
# calling ((x + 2) * x) with [1 3] gives (1 + 2) * 3 = 3 * 3 = 9
# calling (4 * (x / 2)) with [5]   gives 4 * (5 / 2) = 4 * 2 = 8
# All inputs and outputs to/from the expression will be integer types. All expressions tested in this kata will be valid, i.e. there will be no division by zero and the number of values passed in will always be the same as the number of placeholders.
#
# Note: eval and exec are disabled
#
# Algorithms
# Solution
class Placeholder:
    def __init__(self, fn=None):
        self.fn = fn or (lambda args: (args[0], args[1:]))

    def __call__(self, *args):
        value, remaining = self.fn(list(args))
        return value

    def _binop(self, other, op):
        if not isinstance(other, Placeholder):
            other = Placeholder(lambda args, v=other: (v, args))

        def fn(args):
            v1, rest = self.fn(args)
            v2, rest = other.fn(rest)
            return op(v1, v2), rest

        return Placeholder(fn)

    def __add__(self, other):
        return self._binop(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._binop(other, lambda a, b: a - b)

    def __mul__(self, other):
        return self._binop(other, lambda a, b: a * b)

    def __floordiv__(self, other):
        return self._binop(other, lambda a, b: a // b)

    def __radd__(self, other):
        return Placeholder(lambda args, v=other: (v, args)).__add__(self)

    def __rsub__(self, other):
        return Placeholder(lambda args, v=other: (v, args)).__sub__(self)

    def __rmul__(self, other):
        return Placeholder(lambda args, v=other: (v, args)).__mul__(self)

    def __rfloordiv__(self, other):
        return Placeholder(lambda args, v=other: (v, args)).__floordiv__(self)


x = Placeholder()