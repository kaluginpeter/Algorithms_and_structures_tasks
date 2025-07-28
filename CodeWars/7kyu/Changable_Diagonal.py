# I do not claim any authoring rights for this task. This kata was purely inspired by UNT testmakers.
#
# On June 14th, 2025, I took my first ever UNT exam (United National Testing - the main exam in Kazakhstan). On that day, I faced this beginner-friendly task that I wanted to publish here.
#
# Task
# Given a matrix (NxN) and a specific value.
#
# Input:
#
# matrix = [[1,  2,  3,   4],
#           [5,  6,  7,   8],
#           [9,  10, 11, 12],
#           [13, 14, 15, 16]]
#
# value = 2
# What this value does is it changes the main diagonal of the matrix. If value > 0, then the main diagonal drops down, if value < 0, the main diagonal goes up and if value = 0, the diagonal does not change. With this example here (I marked the diagonal numbers with *):
#
# [[*1,   2,   3,   4],
#  [ 5,  *6,   7,   8],
#  [ 9,  10, *11,  12],
#  [13,  14,  15, *16]]
#
# The main diagonal here is [1, 6, 11, 16] but with given value:
#
# [[ 1,   2,  3,  4],
#  [ 5,   6,  7,  8],
#  [*9,  10, 11, 12],
#  [13, *14, 15, 16]]
#
# The main diagonal is [9, 14].
#
# In case of the value being negative, for example -2:
#
# [[ 1,  2, *3,  4],
#  [ 5,  6,  7, *8],
#  [ 9, 10, 11, 12],
#  [13, 14, 15, 16]]
#
# The main diagonal is [3, 8].
# With these rules being said, find the sum of the trace of a matrix with the given value. The value will never exceed or reach the length of an array.
#
# Note for Java: The square brackets do not mean ArrayList<ArrayList<Integer>>. You will be dealing with regular int[][].
#
# MatrixAlgorithms