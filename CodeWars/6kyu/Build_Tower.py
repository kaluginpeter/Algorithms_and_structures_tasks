# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
# A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]
# Go challenge Build Tower Advanced once you have finished this :)
#
# STRINGSASCII ARTFUNDAMENTALS
# Solution
def tower_builder(n_floors):
    list = []
    for i in range(n_floors):
        first_elem=''
        second_elem=''
        for j in range(i,n_floors-1):
            first_elem+=' '
        for k in range(2*i+1):
            second_elem+='*'
        list.append(first_elem + second_elem + first_elem)
    return list