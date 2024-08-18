# Array Exchange and Reversing
#
# It's time for some array exchange!
# The objective is simple: exchange the elements of
# two arrays in-place in a way that their new content is also reversed.
#
# # before
# my_list = ['a', 'b', 'c']
# other_list = [1, 2, 3]
#
# exchange_with(my_list, other_list)
#
# # after
# my_list == [3, 2, 1]
# other_list == ['c', 'b', 'a']
# ARRAYSALGORITHMSFUNDAMENTALS
# Solution
def exchange_with(a, b):
    a[:], b[:] = b[::-1], a[::-1]