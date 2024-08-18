# Closure Counter
# Define the function counter that returns a function that returns an increasing value.
# The first value should be 1.
# You're going to have to use closures.
# Example:
# const newCounter = counter();
# newCounter() // 1
# newCounter() // 2
# Closure:
# A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.
#
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
#
# FUNDAMENTALS
# Solution
def counter():
    i = 0
    def inscrease():
        nonlocal i
        i += 1
        return i
    return inscrease