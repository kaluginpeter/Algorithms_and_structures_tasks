# Task
# Changu and Mangu are great buddies. Once they found an infinite paper which had 1,2,3,4,5,6,7,8,......... till infinity, written on it.
#
# Both of them did not like the sequence and started deleting some numbers in the following way.
#
#  First they deleted every 2nd number. So remaining numbers on the paper: 1,3,5,7,9,11..........till infinity. Then they deleted every 3rd number. So remaining numbers on the paper: 1,3,7,9,13,15..........till infinity.. Then they deleted every 4th number. So remaining numbers on the paper: 1,3,7,13,15..........till infinity. Then kept on doing this (deleting every 5th, then every 6th ...) untill they got old and died.
#
# It is obvious that some of the numbers will never get deleted(E.g. 1,3,7,13..) and hence are know to us as survivor numbers.
#
# Given a number n, check whether its a survivor number or not.
#
# Input/Output
# [input] integer n
# 0 < n <= 10^8
#
# [output] a boolean value
# true if the number is a survivor else false.
#
# ALGORITHMS
# Solution
def survivor(n):
    count = 2
    while count <= n:
        if n % count == 0: return False
        n -= n // count
        count += 1
    return True