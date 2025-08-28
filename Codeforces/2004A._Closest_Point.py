# A. Closest Point
# time limit per test2 seconds
# memory limit per test512 megabytes
# Consider a set of points on a line. The distance between two points i
#  and j
#  is |i−j|
# .
#
# The point i
#  from the set is the closest to the point j
#  from the set, if there is no other point k
#  in the set such that the distance from j
#  to k
#  is strictly less than the distance from j
#  to i
# . In other words, all other points from the set have distance to j
#  greater or equal to |i−j|
# .
#
# For example, consider a set of points {1,3,5,8}
# :
#
# for the point 1
# , the closest point is 3
#  (other points have distance greater than |1−3|=2
# );
# for the point 3
# , there are two closest points: 1
#  and 5
# ;
# for the point 5
# , the closest point is 3
#  (but not 8
# , since its distance is greater than |3−5|
# );
# for the point 8
# , the closest point is 5
# .
# You are given a set of points. You have to add an integer point into this set in such a way that it is different from every existing point in the set, and it becomes the closest point to every point in the set. Is it possible?
#
# Input
# The first line contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# Each test case consists of two lines:
#
# the first line contains one integer n
#  (2≤n≤40
# ) — the number of points in the set;
# the second line contains n
#  integers x1,x2,…,xn
#  (1≤x1<x2<⋯<xn≤100
# ) — the points from the set.
# Output
# For each test case, print YES if it is possible to add a new point according to the conditions from the statement. Otherwise, print NO.
#
# Example
# InputCopy
# 3
# 2
# 3 8
# 2
# 5 6
# 6
# 1 2 3 4 5 10
# OutputCopy
# YES
# NO
# NO
# Note
# In the first example, the point 7
#  will be the closest to both 3
#  and 8
# .
#
# In the second example, it is impossible to add an integer point so that it becomes the closest to both 5
#  and 6
# , and is different from both of them.