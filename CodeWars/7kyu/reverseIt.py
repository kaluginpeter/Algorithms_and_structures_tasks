# You have to create a function named reverseIt.
#
# Write your function so that in the case a string or a number is passed in as the data , you will return the data in reverse order. If the data is any other type, return it as it is.
#
# Examples of inputs and subsequent outputs:
#
# "Hello" -> "olleH"
#
# "314159" -> "951413"
#
# [1,2,3] -> [1,2,3]
# FUNDAMENTALS
# Solution
def reverse_it(data):
    return type(data)(str(data)[::-1]) if type(data) in [int, str, float] else data