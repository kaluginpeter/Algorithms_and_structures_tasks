# Your task is to write a function, which takes two arguments and returns a sequence. First argument is a sequence of values, second is multiplier. The function should filter all non-numeric values and multiply the rest by given multiplier.
#
# ARRAYSALGORITHMS
# Solution
def multiply_and_filter(seq, multiplier):
    return [i * multiplier for i in seq if type(i) == int or type(i) == float]