# A. False Alarm
# time limit per test1 second
# memory limit per test256 megabytes
# Yousef is at the entrance of a long hallway with n
#  doors in a row, numbered from 1
#  to n
# . He needs to pass through all the doors from 1
#  to n
#  in order of numbering and reach the exit (past door n
# ).
#
# Each door can be open or closed. If a door is open, Yousef passes through it in 1
#  second. If the door is closed, Yousef can't pass through it.
#
# However, Yousef has a special button which he can use at most once at any moment. This button makes all closed doors become open for x
#  seconds.
#
# Your task is to determine if Yousef can pass through all the doors if he can use the button at most once.
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains two integers n,x
#  (1≤n,x≤10
# ) — the number of doors and the number of seconds of the button, respectively.
#
# The second line of each test case contains n
#  integers a1,a2,...,an
#  (ai∈{0,1}
# ) — the state of each door. Open doors are represented by '0', while closed doors are represented by '1'.
#
# It is guaranteed that each test case contains at least one closed door.
#
# Output
# For each test case, output "YES" if Yousef can reach the exit, and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 7
# 4 2
# 0 1 1 0
# 6 3
# 1 0 1 1 0 0
# 8 8
# 1 1 1 0 0 1 1 1
# 1 2
# 1
# 5 1
# 1 0 1 0 1
# 7 4
# 0 0 0 1 1 0 1
# 10 3
# 0 1 0 0 1 0 0 1 0 0
# OutputCopy
# YES
# NO
# YES
# YES
# NO
# YES
# NO
# Note
# In the first test case, the optimal way is as follows:
#
# At time 0
# , the door is open, so Yousef passes.
# At time 1
# , the door is closed, Yousef can use the button now and pass through the door.
# At time 2
# , the button's effect is still on, so Yousef can still pass.
# At time 3
# , the button's effect has finished, but the door is open. Yousef passes and reaches the exit.
# In the second test case, Yousef has a 3-second button, but he would need at least a 4-second button to reach the exit. Therefore, the answer is NO.
#
# In the third test case, Yousef can turn on the button before starting to move. All the doors will stay open until he reaches the exit.