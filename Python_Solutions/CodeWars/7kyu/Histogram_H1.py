# Kata in this series
#
# Histogram - H1
# Histogram - H2
# Histogram - V1
# Histogram - V2
# Background
# A 6-sided die is rolled a number of times and the results are plotted as a character-based histogram.
#
# Example:
#
# 6|##### 5
# 5|
# 4|# 1
# 3|########## 10
# 2|### 3
# 1|####### 7
# Task
# You will be passed the dice value frequencies, and your task is to write the code to return a string representing a histogram, so that when it is printed it has the same format as the example.
#
# Notes
# There are no trailing spaces on the lines
# All lines (including the last) end with a newline \n
# A count is displayed beside each bar except where the count is 0
# The number of rolls may vary but there are never more than 100
# STRINGSALGORITHMS
# Solution
def histogram(results):
    return "".join("{}|{} {}\n".format(7 - i, f * "#", f) for i, f in enumerate(results[::-1], 1)).replace(" 0", "")