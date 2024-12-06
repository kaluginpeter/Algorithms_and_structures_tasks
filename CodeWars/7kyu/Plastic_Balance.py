# You will get a list with several scattered numbers
#
# You must check that the sum of the two values on both sides equals the sum of the rest of the list elements
#
# And if not, delete the two elements on the sides and check repeatedly,
#
# until you reach the condition checklist:
#
# The sum of the list without the sides = the sum of the sides
#
# If it never equals return an empty list []
#
# note: list length can be up to 500 items
#
# Example:
# Ex1:
#
# [1,2,3,4,5] ==> 1+5 != 2+3+4 ==> [2,3,4] ==> 2+4 != 3 == [3] ==> 3+3 != 0 ==> []
# note: (3+3) because 3 is first side and last side... (!= 0) because sum of list without sides = 0
#
# Ex2:
#
# [0,104,3,101,0,111] ==> 0+111 != 104+3+101+0 ==> [104,3,101,0] ==> 104+0 = 3+101 ==> [104,3,101,0]
# Ex3:
#
# [1,-1] ==> 1-1 = 0 ==> [1,-1]
# note: (1-1) because 1 is first side and -1 is last side... (= 0) because sum of list without sides (1, -1) = 0
#
# FundamentalsAlgorithmsListsData StructuresArrays