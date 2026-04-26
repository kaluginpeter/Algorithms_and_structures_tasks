# Task
# You are given an 2D array arr, find out the largest "X" hidden in the array.
#
# Rules
# A "X" in the 2D array like this:
#
# [
# ["X"," "," "," ","X"],
# [" ","X"," ","X"," "],
# [" "," ","X"," "," "],
# [" ","X"," ","X"," "],
# ["X"," "," "," ","X"]
# ]
# Of course, the "X" can also be made of other letters:
#
# [
# ["A"," "," "," ","A"],
# [" ","A"," ","A"," "],
# [" "," ","A"," "," "],
# [" ","A"," ","A"," "],
# ["A"," "," "," ","A"]
# ]
# Of course, the location of the space can also be other characters, so it is more difficult to distinguish:
#
# [
# ["A","B","C","D","A"],
# ["P","A","Q","A","E"],
# ["N","O","A","H","F"],
# ["M","A","K","A","G"],
# ["A","L","J","I","A"]
# ]
# Can you find this "X"? Please return the location of the center of "X" using an array [row,column].
#
# If there are more than one "X" in the array, you should return the location of the largest "X"; If there are two or more "X" have the same length, please return the first one(In order from top to bottom, from left to right); If no "X" found, return []
#
# See more examples in the example testcases ;-)
#
# PuzzlesGames