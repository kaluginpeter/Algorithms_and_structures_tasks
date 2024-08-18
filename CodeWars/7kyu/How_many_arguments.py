# Create a function args_count, that returns the count of passed arguments
#
# args_count(1, 2, 3) -> 3
# args_count(1, 2, 3, 10) -> 4
# FUNDAMENTALS
# Solution
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)