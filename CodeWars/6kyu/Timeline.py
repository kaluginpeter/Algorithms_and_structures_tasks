# Have a look at this random graph:
#
# Random graph
#
# For sure, it represents something. A smooth change of some value between May 20th, 2007 and May 28th, 2007, but the value itself doesn't bother us. The timeline does.
#
# I want to know exactly what date and time is, for example, at this point on the graph.
#
# Image with highlighted point
#
# Looks like the red line finds itself somewhen in the evening of May 25th?.. Not sure about the exact time, but that's why you're here!
#
# For simplicity's sake, let's assume this graph is 500 pixels wide (x = 0 is the leftmost point of the curve, matches the May 20th, 2007 0:00, x = 500 is on the farthest right, corresponding to May 28th, 2007 0:00) and the red line is on x = 350.
#
# 350/500 = 0.7, or 70% into the timespan from 2007-05-20 to 2007-05-28. This is exactly 2007-05-25 14:24.
#
# Your task is to implement a function that takes the lower and upper bounds of a timeline, the width of the graph in pixels, and the position of the red line in pixels and returns an ISO formatted string representing the date that the red line is pointed at, with seconds stripped (e.g., "2007-05-25T14:24")
#
# Function Arguments
# start: datetime.datetime object representing a date from which the timeline displays data (in the above example it's 2007-05-20T00:00:00 in ISO format)
# end: datetime.datetime object representing the latest date the timeline displays data for (in the above example it's 2007-05-28T00:00:00 in ISO format)
# width: integer value representing the visual width of the graph in pixels (in the above example it's 500)
# pos: integer value representing the position of the red line in pixels, relative to the graph (in the above example it's 350)
# Constraints
# 1800
# ≤
# y
# e
# a
# r
# ≤
# 2100
# 1800≤year≤2100
# 100
# ≤
# w
# i
# d
# t
# h
# ≤
# 10000
# 100≤width≤10000
# 0
# ≤
# p
# o
# s
# ≤
# w
# i
# d
# t
# h
# 0≤pos≤width
# s
# t
# a
# r
# t
# <
# e
# n
# d
# start<end
# Date Time
# Solution
from datetime import timedelta

def get_date(start, end, width, pos):
    x = (end - start).total_seconds()
    y = x / width * pos
    z = start + timedelta(seconds=y)
    return z.strftime('%Y-%m-%dT%H:%M')