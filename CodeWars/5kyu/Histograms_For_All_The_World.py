# source: imgur.com
#
# A certain university has been doing histograms with the student's results at the end of the course. We are going to explain the statistical procedure of this Institution using the results of a small class of advanced students. The following are the results (percentage rounded, no decimals) of 40 students:
#
# 73 82 70 74 87 69 22 49 73 52
# 86 45 19 15 2 51 3 23 42 50
# 69 58 89 71 59 70 47 41 51 71
# 67 69 60 38 74 56 67 56 46 70
# The results should be sorted:
# 2 3 15 19 22 23 38 41 42 45
# 46 47 49 50 51 51 52 56 56 58
# 59 60 67 67 69 69 69 70 70 70
# 71 71 73 73 74 74 82 86 87 89
# We count the number of elements, n.
# In our case n = 40
#
# We determine the minimum and maximum results. Then, the range of results.
# In our case, min = 2  and max = 89
#
# Then the range is:
#
# range = max - min = 89 - 2 = 87
# The number of intervals or classes, denoted as k, is determined using the Sturges' rule, which employs the base 10 logarithm (log10):
# k = 1 + 3.32 * log10 (n)
# In our case: k = 1 + 3.32 * log10 (40) = 6.3189
# The value of k should be rounded to an integer value, so k = 6.
#
# The amplitude, A, of each class or interval is determined by:
# A = range / k
# In our case: A = 87 / 6 = 14.5
# Let's take the ceiling of A, so A = 15.0
#
# We determine the values for the classes:
#
# min -----> min + A -----> min + 2A -----> min -----> min + 3A ----->...-----> min + kA
# In our case will be :
#
# 2 ----> 17 ----> 32 ----> 47----> 62----> 77----> 92
# Now we have to determine the lower and upper bounds for each intervals. Our variable is discrete (rounded percentages), so it would be:
#
# lower       upper    dif
#   2           16     14
#   17          31     14
#   32          46     14
#   47          61     14
#   62          76     14
#   77          92     15
# Now we have to determine the frequencies, F each class or interval has
#
# Num. of class     lower       upper  values                                        F
#  1              2           16   2, 3, 15                                      3
#  2             17           31   19, 22, 23                                    3
#  3             32           46   38,41,42,45,46                                5
#  4             47           61   47,49,50,51,51,52,56,56,58,59,60             11
#  5             62           76   67,67,69,69,69,70,70,70,71,71,73,73,74,74    14
#  6             77           92   82,86,87,89                                   4
# Finally, it should be calculated the accumulated frequency Fa+, for each class (last column). It would be:
#
# Num. of class     lower       upper     F       Fa+
#   1              2           16      3        3
#   2             17           31      3        6
#   3             32           46      5       11
#   4             47           61     11       22
#   5             62           76     14       36
#   6             77           92      4       40
# The accumulated frequency for a class, is the amount of values that are beloww the upper bound of this class.
#
# This university prepared a MOOC course and they estimate a number of 80000 students worldwide to take the course. They have been doing this work manually but now they need a code.
#
# Could you help in creating a code to do the histograms for thousands of students?
#
# For that task we need a function, let's name it  hist_maker() , will receive an array of results for each student and will have to output the a list of lists, each of these lists having the result of the classes in order to make a graph. The data for each class:
#
# [Num. of class, [lower, upper], F, Fa+]
# For arrays with a lot of elements we should have that the lower bound will be equal to upper bound(will be a value) and the output should be reduced to appear the percentage value twice:
#
# [Num. of class, [value, value], F, Fa+]
# For our case will be:
#
# students_results = [73, 82, 70, 74, 87, 69, 22, 49, 73, 52,
# 86, 45, 19, 15, 2, 51, 3, 23, 42, 50,
# 69, 58, 89, 71, 59, 70, 47, 41, 51, 71,
# 67, 69, 60, 38, 74, 56, 67, 56, 46, 70]
#
# hist_maker(students_results) == [[1, [2, 16], 3, 3], [2, [17, 31], 3, 6], [3, [32, 46], 5, 11], [4, [47, 61], 11, 22], [5, [62, 76], 14, 36], [6, [77, 92], 4, 40]]
# Three important tips:
#
# If ΣF ≠ n something has to be wrong.
#
# In our case ΣF = 3 + 3 + 5 + 11 + 14 + 4 = 40
#
# If Fa+ for the last class is different from n (number of elements introduced)
# something has to be wrong.
#
# In our case for the 6-th class is 40.
#
# The upper bound can't be higher than 100, so your code should correct every upper bound more than 100. Suposee that the interval for the last obtained using Sturges'rule is  [97, 102] , it should be  [97, 100]
#
# 10 <= len(students_results) <= 10^5
#
# Enjoy it!!
#
# AlgorithmsMathematicsStatisticsData SciencePerformance
# Solution
from math import log10, ceil

def hist_maker(students_results):
    students_results.sort()
    n: int = len(students_results)
    mn: int = students_results[0]
    mx: int = students_results[-1]
    rng: int = mx - mn
    k: int = round(1 + 3.32 * log10(n))
    A: int = ceil(rng / k)
    output: list[list[int, list[int, int], int, int]] = []
    idx: int = 0
    for i in range(rng // A + (rng % A != 0)):
        f: int = 0
        upper: int = min(100, mn + A - (1 if mn + A < mx else 0))
        while idx < n and students_results[idx] <= upper:
            f += 1
            idx += 1
        output.append([i + 1, [mn, upper], f, f + (0 if not output else output[-1][-1])])
        mn += A
    return output