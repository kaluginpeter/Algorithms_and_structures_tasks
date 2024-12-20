# Problem description
# Mr. Strolly lives in a fancy neighborhood called Gridsville. Once a day he likes to take a walk. Since his neighborhood is a grid, he can either walk in the directions of North(n), East(e), South(s) or West(w). Mr. Strolly's problem is that he often goes on long walks and can't remember exactly where he is. Even when he can remember the path he took, when he is ready to go home, he wants to take the shortest path.
#
# Task
# Can you write a class to help him keep track of where he is?
#
# Your job is to write a class 'Walker()'. This class should have a couple of methods:
#
# 1: 'walk'
# a method that takes in a string containing the directions of the 'path' that Mr. Strolly walked.
# 2: 'coords'
# a method that will tell Mr. Strolly where he is with respect to his house.
# Notes:
#
# Mr. Strolly's 'coords' should return a tuple in the format (x-coordinate,y-coordinate), revealing how far away from home he is (e/w,n/s)
# Only valid walks consisting of lowercase e,s,w,n will be tested.
# e = x+1, w = x-1, likewise n = y+1, s = y-1
# Example:
#
# a walk of 'eess' should return (2,-2)
# Help Mr. Strolly find out where he is!
#
# While this task doesn't necessarily require a class, it is meant to practice writing classes.
#
# Object-oriented ProgrammingFundamentals