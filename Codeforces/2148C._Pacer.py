# C. Pacer
# time limit per test2 seconds
# memory limit per test256 megabytes
# The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. A single lap should be completed every time you hear this sound. Ding! Remember to run in a straight line and run as long as possible. The test will begin on the word start. On your mark. Get ready!...
#
# Farmer John is running the FitnessGram Pacer Test! Farmer John takes one minute to run to the other side of the gym. Therefore, at the start of each minute, FJ can choose to either run to the other side of the gym or stay in place. If he chooses to run to the other side of the gym, he gains one point.
#
# FJ will run the Pacer Test until the start of the m
# -th minute. Initially (at the start of the 0
# -th minute), FJ is at the starting side of the gym, which we will denote as side 0
# . The opposite side of the gym is denoted side 1
# .
#
# The pacer test audio plays n
#  times. At the start of the ai
# -th minute, FJ must be at the bi
# -th side of the gym.
#
# What is the maximum number of points FJ can acquire while ensuring that he meets the audio's requirements?
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and m
#  (1≤n≤2⋅105,n≤m≤109
# ) — the number of requirements and the number of total minutes.
#
# The following n
#  lines contain two integers ai
#  and bi
#  (1≤ai≤m,bi∈{0,1})
#  — the i
# -th requirement by the audio. It is guaranteed that ai>ai−1
#  over all i>1
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output the maximum number of points that FJ can acquire.
#
# Example
# InputCopy
# 3
# 2 4
# 2 1
# 4 0
# 2 7
# 1 1
# 4 0
# 4 9
# 1 0
# 2 0
# 6 1
# 9 0
# OutputCopy
# 2
# 7
# 6
# Note
# For the first sample test case,
#
# During minute 0
# , FJ can stay at side 0
# .
# During minute 1
# , FJ can run to side 1
#  and gain 1
#  point.
# Right before minute 2
# , the audio requires FJ to be at side 1
# . Here, FJ is indeed at side 1
# .
# During minute 2
# , FJ can run to side 0
#  and gain 1
#  point.
# During minute 3
# , FJ can stay at side 0
# .
# Right before minute 4
# , the audio requires FJ to be at side 0
# . Here, FJ is indeed at side 0
# .
# Since the start of minute 4
#  has reached, the Pacer Test ends. His total score is 2
# .
# Relevant illustration of the statement: