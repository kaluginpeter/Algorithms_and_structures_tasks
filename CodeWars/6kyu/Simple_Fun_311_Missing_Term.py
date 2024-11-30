# Task
# Little Chou has just learnt how to count and add numbers.
#
# So his dad gave him an exercise to add all the terms of a finite sequence a, a + 1, a + 2, a + 3....
#
# Little Chou is a very intelligent boy but he was distracted while doing the exercise. He left out EXACTLY one term of the sequence. He is a kid after all!
#
# His dad easily spotted which term his son left out. Can you?
#
# Example
# For n = 1 and littleChouSum = 4, the output should be 2.
#
# Here the first term is 1, and the sum that Little Chou calculates is 4. He forgot to add the 2nd term, which is 2.
#
# 1 + missedTerm + 3 = 4
#
# For n = 4 and littleChouSum = 35, the output should be 4.
#
# Little Chou forgot to add the 1st term, which is 4.
#
# missedTerm + 5 + 6 + 7 + 8 + 9 = 35
#
# Input/Output
# [input] integer n
#
# The first term of the sequence.
#
# 1 ≤ n ≤ 10^4
#
# [input] integer littleChouSum
#
# The sum that little Chou ended up with.
#
# 0 ≤ littleChouSum ≤ 10^9
#
# [output] an integer
#
# The term that little Chou left out in his exercise.
#
# Fundamentals
# Solution
def missing_term(n, little_chou_sum):
    term: int = n
    valid_sum: int = 0
    while little_chou_sum >= valid_sum:
        valid_sum += term
        term += 1
    return valid_sum - little_chou_sum