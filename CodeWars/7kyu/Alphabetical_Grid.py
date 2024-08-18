# Task:
# You need to write a function grid that returns an alphabetical grid of size NxN, where a = 0, b = 1, c = 2....
#
# Examples:
# grid(4)
#
# a b c d
# b c d e
# c d e f
# d e f g
# grid(10)
#
# a b c d e f g h i j
# b c d e f g h i j k
# c d e f g h i j k l
# d e f g h i j k l m
# e f g h i j k l m n
# f g h i j k l m n o
# g h i j k l m n o p
# h i j k l m n o p q
# i j k l m n o p q r
# j k l m n o p q r s
# Notes:
# After "z" comes "a"
# If function receive N < 0 should return:
# None
# FUNDAMENTALSALGORITHMS
# Solution
def grid(N):
    if N < 0: return None
    if N == 0: return ''
    al, word = 'abcdefghijklmnopqrstuvwxyz' * N, []
    for i in range(N):
        top = [' '.join(al[i: i + N])]
        word.append(' '.join(top))
    return '\n'.join(word)