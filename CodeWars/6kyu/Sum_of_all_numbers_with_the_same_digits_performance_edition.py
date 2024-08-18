# Description
# Find the sum of all numbers with the same digits (permutations) as the input number, including duplicates. However, due to the fact that this is a performance edition kata, the input can go up to 10**10000. That's a number with 10001 digits (at most)! Be sure to use efficient algorithms and good luck! All numbers tested for will be positive.
#
# Examples
# 98    -->  187    ;  89 + 98  =  187
# 123   -->  1332   ;  123 + 132 + 213 + 231 + 312 + 321  =  1332
# 1185  -->  99990  ;  1185 + 1158 + 1815 + 1851 + 1518 + 1581 + 1185 + 1158 + 1815 +
#                    + 1851 + 1518 + 1581 + 8115 + 8151 + 8115 + 8151 + 8511 + 8511 +
#                    + 5118 + 5181 + 5118 + 5181 + 5811 + 5811  =  99990
# PERFORMANCEPERMUTATIONSFUNDAMENTALS
# Solution
from math import factorial
def sum_arrangements(n):
    w = str(n)
    return (10**len(w)-1)//9*sum(map(int,w))*factorial(len(w)-1)