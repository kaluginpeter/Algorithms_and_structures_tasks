# In this kata, you are given the sum of the number of vertices, edges, and faces of an
#
# N-sided pyramid, which is equal to s. You need to return the number of vertices,edges,
#
# faces, and the number of sides of the base of the pyramid.
#
# MATHEMATICSALGORITHMS
# Solution
def pyramid(s):
    N = (s - 2) // 4
    V = N + 1
    E = 2 * N
    F = N + 1
    return (V, E, F, N)