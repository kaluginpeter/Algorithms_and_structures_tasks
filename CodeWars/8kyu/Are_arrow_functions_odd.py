# Time to test your basic knowledge in functions! Return the odds from a list:
#
# [1, 2, 3, 4, 5]  -->  [1, 3, 5]
# [2, 4, 6]        -->  []
# FUNDAMENTALS
# Solution
odds = lambda list: [i for i in list if i % 2 !=0]
