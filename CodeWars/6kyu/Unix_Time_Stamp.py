# Background
# Unix Time Stamp is a date and time representation widely used in computing.
#
# It measures time by the number of non-leap seconds that have elapsed since 00:00:00 UTC on 1st January 1970.
#
# In modern computing, values are sometimes stored with higher granularity, such as microseconds or nanoseconds (In this kata, you just need to be accurate to the second).
#
# Task
# Complete the function to convert the given time to unix time stamp.
#
# Notes
# Leap days should be taken into account
# import is disabled in Python
# Examples
# [1970, 1, 1, 0, 0, 0]       -->  0
# [2001, 9, 9, 1, 46, 40]     -->  1000000000
# [2345, 6, 7, 8, 9, 10]      -->  11847456550
# [9999, 12, 31, 23, 59, 59]  -->  253402300799
# Input/Output
# Type of input : List/Array/Table (Depends on language)
# Elements : [Year, Month, Day, Hour, Minute, Second]
# Range : [1970-9999, 1-12, 1-31, 0-23, 0-59, 0-59]
# All inputs are valid
# For translators
# Functions that directly complete kata should be disable in all languages
#
# Date Time