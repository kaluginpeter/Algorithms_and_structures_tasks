# Given an array with 3 subarrays, each containing hexadecimal color codes loosely defining red, green and blue colors based on their predominant byte value, return a string description of which of the three colors each array contains.
#
# Input is an array which contains 3 subarrays. These subarrays contain strings representing colors in RGB format, each string will contain one predominant color channel that is more saturated than the other two. Among all the strings in an subarray only 2 color channels will come up as predominant - the one that appears more often is "major" and the one that appears less often is "minor". Your task is to determine the major and minor colors inside each subarray and return them in the following format: {Major1}+{Minor1},{Major2}+{Minor2},{Major3}+{Minor3}.
#
# Example:
#
# input = [
#   ["FFA07A", "FA8072", "8DC4DE"],
#   ["7FFF00", "ADFF2F", "FF0000", "00FF7F", "00FF7F"],
#   ["ADD8E6", "6B8E23", "9ACD32", "32CD32", "00FF00"]
# ]
#
# result = "Red+Blue,Green+Red,Green+Blue"
# Explanation:
#
# first subarray's predominant colors: Red, Red, Blue (Red is major, Blue is minor)
# second subarray's predominant colors: Green, Green, Red, Green, Green (Green is major, Red is minor)
# third subarray's predominant colors: Blue, Green, Green, Green, Green (Green is major, Blue is minor)
# FUNDAMENTALSARRAYS
# Solution
from PIL import ImageColor
def get_colors(col_arr):
    l: list = []
    for j in col_arr:
        d: dict = {}
        for k in j:
            r, g, b = ImageColor.getcolor('#' + k, "RGB")
            mx = max(r, g, b)
            if mx == r:
                d['Red'] = d.get('Red', 0) + 1
            elif mx == g:
                d['Green'] = d.get('Green', 0) + 1
            else:
                d['Blue'] = d.get('Blue', 0) + 1
        l.append(f"{max(d, key=d.get)}+{min(d, key=d.get)}")
    return ','.join(l)