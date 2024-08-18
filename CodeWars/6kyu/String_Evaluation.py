# Evaluate the given string with the given conditons.
#
# The conditions will be passed in an array and will be formatted like this:
#
# {symbol or digit}{comparison operator}{symbol or digit}
# Return the results in an array.
#
# The characters in the conditions will always be in the string. Characters in the string are chosen from ascii letters + @#$%^&*()_{}[]
#
# Example
# input string: "aab#HcCcc##l#"
# conditions: ["a<b", "#==4", "c>=C", "H!=a"]
# The conditions in this example array can be interpreted as:
#
# "a<b": The number of times "a" occurs in the string should be less than the number of times "b" occurs in the string
# "#==4": "#" should occur exactly 4 times in the string
# "c>=C": "c" should occur greater than or equal to the number of times "C" occurs
# "H!=a": The number of times "H" occurs should not equal the number of times "a" occurs
# In this example condition 1 is false and 2, 3, 4 are true. So the return value will be an array as such:
#
# [False, True, True, True]
# STRINGSALGORITHMS
# Solution
def string_evaluation(s, w):
    return [eval(f"{(s.count(i[0]), i[0])[i[0].isdigit()]} {i[1:-1]} {(s.count(i[-1]), i[-1])[i[-1].isdigit()]}") for i in w]