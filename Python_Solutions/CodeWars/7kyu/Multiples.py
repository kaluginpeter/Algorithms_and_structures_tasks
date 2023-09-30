# Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3, "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5, and "Miss" if it isn't divisible by any of them. Note: Your program should only return one value
#
# Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom"
#
# FUNDAMENTALS
# Solution
def multiple(x):
    return 'Bang' if x%3==0 and x%5!=0 else 'Boom' if x%3!=0 and x%5==0 else 'BangBoom' if x%3==0 and x%5==0 else 'Miss'