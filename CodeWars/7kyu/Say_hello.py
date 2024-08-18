# Say hello!
#
# Write a function to greet a person. Function will take name as input and greet the person by saying hello. Return null/nil/None if input is empty string or null/nil/None.
#
# Example:
#
# greet("Niks") --> "hello Niks!"
# greet("")    --> None # Return None if input is empty string
# greet(None)  --> None # Return None if input is None
# FUNDAMENTALS
# Solution
def greet(name):
    return f"hello {name}!" if name else None