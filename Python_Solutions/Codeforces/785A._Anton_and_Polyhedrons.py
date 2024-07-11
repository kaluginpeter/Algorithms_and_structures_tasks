# A. Anton and Polyhedrons
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Anton's favourite geometric figures are regular polyhedrons. Note that there are five kinds of regular polyhedrons:
#
# Tetrahedron. Tetrahedron has 4 triangular faces.
# Cube. Cube has 6 square faces.
# Octahedron. Octahedron has 8 triangular faces.
# Dodecahedron. Dodecahedron has 12 pentagonal faces.
# Icosahedron. Icosahedron has 20 triangular faces.
# All five kinds of polyhedrons are shown on the picture below:
#
#
# Anton has a collection of n polyhedrons. One day he decided to know, how many faces his polyhedrons have in total. Help Anton and find this number!
#
# Input
# The first line of the input contains a single integer n (1 ≤ n ≤ 200 000) — the number of polyhedrons in Anton's collection.
#
# Each of the following n lines of the input contains a string si — the name of the i-th polyhedron in Anton's collection. The string can look like this:
#
# "Tetrahedron" (without quotes), if the i-th polyhedron in Anton's collection is a tetrahedron.
# "Cube" (without quotes), if the i-th polyhedron in Anton's collection is a cube.
# "Octahedron" (without quotes), if the i-th polyhedron in Anton's collection is an octahedron.
# "Dodecahedron" (without quotes), if the i-th polyhedron in Anton's collection is a dodecahedron.
# "Icosahedron" (without quotes), if the i-th polyhedron in Anton's collection is an icosahedron.
# Output
# Output one number — the total number of faces in all the polyhedrons in Anton's collection.
#
# Examples
# inputCopy
# 4
# Icosahedron
# Cube
# Tetrahedron
# Dodecahedron
# outputCopy
# 42
# inputCopy
# 3
# Dodecahedron
# Octahedron
# Octahedron
# outputCopy
# 28
# Note
# In the first sample Anton has one icosahedron, one cube, one tetrahedron and one dodecahedron. Icosahedron has 20 faces, cube has 6 faces, tetrahedron has 4 faces and dodecahedron has 12 faces. In total, they have 20 + 6 + 4 + 12 = 42 faces.