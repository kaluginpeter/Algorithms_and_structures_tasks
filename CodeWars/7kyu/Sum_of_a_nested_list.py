# Implement a function to calculate the sum of the numerical values in a nested list. For example :
#
# sum_nested([1, [2, [3, [4]]]]) -> 10
# RECURSIONLISTSALGORITHMSFUNDAMENTALS
# Solution
def sum_nested(lst):
	return sum(sum_nested(x) if isinstance(x,list) else x for x in lst)