# A square matrix is considered upper-triangular if all the entries below the main diagonal are 0. Similarly, a square matrix is considered lower-triangular if all the entries above the main diagonal are 0.
#
# Given a square matrix of size n > 1, determine if it is upper triangular or lower triangular. The matrix (mat) is represented by a nested array of rows.
#
# In Ruby, Matrix is disabled
# Examples
#
# upper_triangular([[1,1,1],[0,1,1],[0,0,1]]) # => true
# upper_triangular([[0,0,0],[0,0,0],[1,0,0]]) # => false
# lower_triangular([[1,0],[1,1]]) # => true
# lower_triangular([[0,1],[0,0]]) # => false
# http://en.wikipedia.org/wiki/Triangular_matrix
#
# MatrixLinear AlgebraAlgorithms
# Solution
def upper_triangular(mat):
    n: int = len(mat)
    return all(
        mat[i][j] == 0
        for i in range(n)
        for j in range(i)
    )


def lower_triangular(mat):
    n: int = len(mat)
    return all(
        mat[i][j] == 0
        for i in range(n)
        for j in range(i + 1, n)
    )