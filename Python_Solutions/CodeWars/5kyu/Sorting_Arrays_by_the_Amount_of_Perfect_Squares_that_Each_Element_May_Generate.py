# You will be given an array of positive integers. The array should be sorted by the amount of distinct perfect squares and reversed, that can be generated from each number permuting its digits.
#
# E.g.: arr = [715, 112, 136, 169, 144]
#
# Number   Perfect Squares w/ its Digits   Amount
#  715                -                       0
#  112               121                      1
#  136               361                      1
#  169           169, 196, 961                3
#  144             144, 441                   2
# So the output will have the following order: [169, 144, 112, 136, 715]
#
# When we have two or more numbers with the same amount of perfect squares in their permutations, we sorted by their values.
#
# In the example given above, we can see that 112 and 136 both generate a perfect square. So 112 comes first.
#
# Examples for this kata:
#
# sort_by_perfsq([715, 112, 136, 169, 144]) == [169, 144, 112, 136, 715]
# # number of perfect squares:                   3    2    1    1    0
# We may have in the array numbers that belongs to the same set of permutations.
#
# sort_by_perfsq([234, 61, 16, 441, 144, 728]) == [144, 441, 16, 61, 234, 728]
# # number of perfect squares:                      2    2    1   0   0    0
# Features of the random tests:
#
# Number of tests: 80
# Arrays between 4 and 20 elements
# Integers having from 1 to 7 digits included
# Enjoy it!!
#
# ALGORITHMSMATHEMATICSNUMBER THEORYPERMUTATIONS