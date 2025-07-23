# We are interested in collecting the triples of positive integers (a, b, c) that fulfill the following equation:
#
# a² + b² = c³
# The first triple with the lowest values that satisfies the equation we have above is (2, 2 ,2). In effect:
#
# 2² + 2² = 2³
# 4  + 4  = 8
# The first pair of triples that "shares" the same value of c is: (2, 11, 5) and (5, 10, 5).
#
# Both triples share the same value of c is c = 5.
#
# Triple (2, 11, 5)                  Triple(5, 10, 5)
# 2² + 11² =  5³                      5² +  10²  =  5³
# 4  + 121 = 125                     25  + 100   = 125
# So, we say that the value c has two solutions because there are two triples sharing the same value of c.
#
# There are some values of c with no solutions.
#
# The first value of c that have a surprising number of solutions is 65 with 8 different triples.
#
# In order to avoid duplications you will consider that a <= b always.
#
# Make the function find_abc_sumsqcube(), that may give us the values of c for an specific number of solutions.
#
# For that purpose the above required function will receive two arguments, c_max and num_sol. It is understandable that c_max will give to our function the upper limit of c and num_sol, the specific number of solutions.
#
# The function will output a sorted list with the values of c that have a number of solutions equals to num_sol
#
# Let's see some cases:
#
# find_abc_sumsqcube(5, 1) == [2] # below or equal to c_max = 5 we have triple the (2, 2, 2) (see above)
#
# find_abc_sumsqcube(5, 2) == [5] # now we want the values of ```c ≤ c_max``` with two solutions (see above again)
#
# find_abc_sumsqcube(10, 2) == [5, 10]
#
# find_abc_sumsqcube(20, 8) == [] # There are no values of c equal and bellow 20 having 8 solutions.
# Our tests will have the following ranges for our two arguments:
#
# 5 ≤ c_max ≤ 1000
# 1 ≤ num_sol ≤ 10
# Happy coding!!
#
# FundamentalsAlgorithmsData StructuresMathematicsMemoization