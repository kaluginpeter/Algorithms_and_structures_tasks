# You know combinations: for example, if you take 5 cards from a 52 cards deck you have 2,598,960 different combinations.
#
# In mathematics the number of x combinations you can take from a set of n elements is called the binomial coefficient of n and x, or more often n choose x. The formula to compute n choose x is:
#
# n! / (x! * (n - x)!)
#
# where ! is the factorial operator.
#
# You are a renowned poster designer and painter. You are asked to provide 6 posters all having the same design each in 2 colors. Posters must all have a different color combination and you have the choice of 4 colors: red, blue, yellow, green. How many colors can you choose for each poster?
#
# The answer is two since 4 choose 2 = 6. The combinations will be: {red, blue}, {red, yellow}, {red, green}, {blue, yellow}, {blue, green}, {yellow, green}.
#
# Now same question but you have 35 posters to provide and 7 colors available. How many colors for each poster? If you take combinations 7 choose 2 you will get 21 with the above formula. But 21 schemes aren't enough for 35 posters. If you take 7 choose 5 combinations you will get 21 too. Fortunately if you take 7 choose 3 or 7 choose 4 combinations you get 35 and so each poster will have a different combination of 3 colors or 4 colors. You will take 3 colors because it's less expensive.
#
# Hence the problem:
# Knowing m (number of posters to design) and n (total number of available colors), let us search x, the number of colors for each poster so that each poster has a unique combination of colors and the number of combinations is exactly the same as the number of posters m.
#
# In other words, you must find x such that:
#
# n choose x = m
#
# for a given m >= 0 and a given n > 0. If there are several solutions, return the smallest. If there are no solutions, return -1.
#
# Examples:
# (m =  6, n = 4) -->  2
# (m =  4, n = 4) -->  1
# (m =  4, n = 2) --> -1
# (m = 35, n = 7) -->  3
# (m = 36, n = 7) --> -1
#
# a = 47129212243960
# (m = a,     n = 50) --> 20
# (m = a + 1, n = 50) --> -1
# COMBINATORICSMATHEMATICS