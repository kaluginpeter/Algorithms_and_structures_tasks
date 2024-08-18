# This kata is about static method that should return different values.
#
# On the first call it must be 1, on the second and others - it must be a double from previous value.
#
# Look tests for more examples, good luck :)
#
# OBJECT-ORIENTED PROGRAMMING
# Solution
class Class:
    count = 1
    def get_number():
        res = Class.count
        Class.count *= 2
        return res