# Problem / Lore
# William is a great beverage merchant from the Middle Ages. Lately, he has noticed that the space in his barrels warehouse is being misused. As he sells different types of beverages, it is common for barrels to be removed and inserted in random positions, leaving several empty spaces of different sizes. So he decided that it was not worth redistributing the barrels and that new barrels should be placed contiguously and in the smallest available space they can fit in.
#
# Challenge Description
# Your task is to create a function that will help William better manage his warehouse, your function receives two parameters:
#
# The first is a array that represents a warehouse of barrels; each character '0' represents a barrel, and an empty string '' represents an available space.
# The second parameter is a array of '0', which are the new barrels to be inserted (they must be inserted together).
# You must find the first smallest available space where the new barrels fit and place them there from left to right. Return the array of barrels with the new barrels inserted.
#
# Examples (input -> output)
# ['0','','','0','','','','0'], ['0','0'] -> ['0','0','0','0','','','','0']
#
# ['0','0','','','0','','','','0'], ['0'] -> ['0','0','0','','0','','','','0']
# More examples in test cases
#
# Notes
# The priority is that the space is as small as possible, so first you must find the smallest spaces that fit, and if there is a tie, place them in the leftmost space.
# When placed, the barrels must be positioned from left to right in the available space.
# If there isn't enough space, return the warehouse unchanged.
# Good luck!
#
# AlgorithmsArrays