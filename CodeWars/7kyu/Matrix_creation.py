# Create an identity matrix of the specified size( >= 0).
#
# Some examples:
#
# (1)  =>  [[1]]
#
# (2) => [ [1,0],
#          [0,1] ]
#
#        [ [1,0,0,0,0],
#          [0,1,0,0,0],
# (5) =>   [0,0,1,0,0],
#          [0,0,0,1,0],
#          [0,0,0,0,1] ]
# FUNDAMENTALSARRAYSMATRIXLINEAR ALGEBRAMATHEMATICSLANGUAGE FEATURES
# Solution
def get_matrix(n):
    mat = [[0] * n for j in range(n)]
    for i in range(len(mat)):
        mat[i][i] = 1
    return mat