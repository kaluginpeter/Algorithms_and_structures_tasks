# A. Shashliks
# time limit per test1 second
# memory limit per test256 megabytes
# You are the owner of a popular shashlik restaurant, and your grill is the heart of your kitchen. However, the grill has a peculiarity: after cooking each shashlik, its temperature drops.
#
# You need to cook as many portions of shashlik as possible, and you have an unlimited number of portions of two types available for cooking:
#
# The first type requires a temperature of at least a
#  degrees at the start of cooking, and after cooking, the grill's temperature decreases by x
#  degrees.
# The second type requires a temperature of at least b
#  degrees at the start of cooking, and after cooking, the grill's temperature decreases by y
#  degrees.
# Initially, the grill's temperature is k
#  degrees. Determine the maximum total number of portions of shashlik that can be cooked.
#
# Note that the grill's temperature can be negative.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The only line of each test case contains five integers k
# , a
# , b
# , x
# , and y
#  (1≤k,a,b,x,y≤109
# ) — the initial temperature of the grill, the required temperature for cooking the first and second types of shashlik, respectively, as well as the temperature drop after cooking the first and second types of shashlik, respectively.
#
# Output
# For each test case, output a single integer — the maximum number of portions of shashlik that you can cook.
#
# Example
# InputCopy
# 5
# 10 3 4 2 1
# 1 10 10 1 1
# 100 17 5 2 3
# 28 14 5 2 4
# 277 5 14 1 3
# OutputCopy
# 8
# 0
# 46
# 10
# 273
# Note
# In the first test case, it is advantageous to cook 7
#  portions of the second type of shashlik; after that, the grill's temperature will be 3
#  degrees, and we can cook one more portion of the first type of shashlik.
#
# In the second test case, we cannot cook either type of shashlik because the grill is too cold.
#
# In the fourth test case, it is advantageous to cook 8
#  portions of the first type of shashlik; after that, it will be possible to cook another 2
#  portions of the second type of shashlik.