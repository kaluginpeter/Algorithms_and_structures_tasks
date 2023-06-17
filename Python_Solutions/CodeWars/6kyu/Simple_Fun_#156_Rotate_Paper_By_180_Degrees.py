# Task
# You are given a digital number written down on a sheet of paper.
#
# Your task is to figure out if you rotate the given sheet of paper by 180 degrees would the number still look exactly the same.
#
# Note: You can assume that the digital number is written like the following image:
#
#
# Example
# For number = "1", the result should be false
#
# For number = "29562", the result should be true.
#
# For number = "77", the result should be false.
#
# Input/Output
# [input] string number
# sequence of digital digits given as a string.
#
# [output] a boolean value
# true if you rotate the given sheet of paper by 180 degrees then the number still look exactly the same. false otherwise.
#
# PUZZLES
# Solution
def rotate_paper(n):
    return n == n.translate(str.maketrans('69', '96', '1347'))[::-1]