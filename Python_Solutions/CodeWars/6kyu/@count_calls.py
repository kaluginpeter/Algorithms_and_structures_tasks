# Implement the "count" decorator, which adds an attribute "call_count" to a function passed in
# to it, and increments it every time the function is called.
#
# The behavior of the decorated function must be the same as before. Your decorator must be well-behaved,
# i.e. the returned function must have the same name and docstring as the original,
# and must be able to handle the same arguments.
#
# Here's an example :
#
# @count_calls
# def multiply(a, b=1):
#     """Calculates the product of a and b."""
#     return a * b
#
# multiply.call_count == 0  # True
#
# for _ in range(3):
#     multiply(1)
#
# multiply.call_count == 3  # True
# FUNDAMENTALS
# Solution
from functools import wraps
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper