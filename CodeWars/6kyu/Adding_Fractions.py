# In most languages, division immediately produces decimal values, and therefore, adding two fractions gives a decimal result:
#
# (1/2) + (1/4) #=> 0.75
# But what if we want to be able to add fractions and get a fractional result?
#
# (1/2) + (1/4) #=> 3/4
# Task:
# Your job here is to implement a function, add_fracs that takes any number of fractions (positive OR negative) as strings, and yields the exact fractional value of their sum in simplest form. If the sum is greater than one (or less than negative one), it should return an improper fraction. If there are no arguments passed, (add_fracs()), return an empty string. Inputs will always be valid fractions, and the output should also be a string. If the result is an integer, like '2/1', just return '2'. Input numerators (but NOT denominators) can be zero.
#
# How the function will be called:
# add_fracs(any_number_of_fractions1, any_number_of_fractions2, any_number_of_fractions3, ...) #=> a fraction as a string
# Some examples (see example test cases for more):
# add_fracs() #=> ""
# add_fracs("1/2") #=> "1/2"
# add_fracs("1/2", "1/4") #=> "3/4"
# add_fracs("1/2", "3/4") #=> "5/4"
# add_fracs("2/4", "6/4", "4/4") #=> "3"
# add_fracs("2/3", "1/3", "4/6") #=> "5/3"
# add_fracs("-2/3", "5/3", "-4/6") #=> "1/3"
# If there are any issues with the description, test cases or anything else, please do let me know by commenting or marking an issue. Otherwise, make sure to rank and mark as ready. Enjoy!
#
# Also check out my other creations — Split Without Loss, Random Integers, Implement String#transpose, Implement Array#transpose!, Arrays and Procs #1, and Arrays and Procs #2
#
# Fundamentals