# A. Download More RAM
# time limit per test1 second
# memory limit per test256 megabytes
# Did you know you can download more RAM? There is a shop with n
#  different pieces of software that increase your RAM. The i
# -th RAM increasing software takes ai
#  GB of memory to run (temporarily, once the program is done running, you get the RAM back), and gives you an additional bi
#  GB of RAM (permanently). Each software can only be used once. Your PC currently has k
#  GB of RAM.
#
# Note that you can't use a RAM-increasing software if it takes more GB of RAM to use than what you currently have.
#
# Since RAM is the most important thing in the world, you wonder, what is the maximum possible amount of RAM achievable?
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤100
# ) — the number of test cases. The description of test cases follows.
#
# The first line of each test case contains the integers n
#  and k
#  (1≤n≤100
# , 1≤k≤1000
# ). Then two lines follow, each containing n
#  integers describing the arrays a
#  and b
#  (1≤ai,bi≤1000
# ).
#
# Output
# For each test case, output a single line containing the largest amount of RAM you can achieve.
#
# Example
# inputCopy
# 4
# 3 10
# 20 30 10
# 9 100 10
# 5 1
# 1 1 5 1 1
# 1 1 1 1 1
# 5 1
# 2 2 2 2 2
# 100 100 100 100 100
# 5 8
# 128 64 32 16 8
# 128 64 32 16 8
# outputCopy
# 29
# 6
# 1
# 256
# Note
# In the first test case, you only have enough RAM to run the third software initially, but that increases your RAM to 20
#  GB, which allows you to use the first software, increasing your RAM to 29
#  GB. The only software left needs 30
#  GB of RAM, so you have to stop here.
#
# In the second test case, you can use the first, second, fourth and fifth software that need only 1
#  GB of RAM per software to run to increase your RAM to 5
#  GB, and then use the last remaining one to increase your RAM to 6
#  GB.
#
# In the third test case, all the software need more than 1
#  GB of RAM to run, so the amount of RAM you have stays at 1
#  GB.