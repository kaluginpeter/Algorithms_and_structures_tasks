# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)
#
# (the dedicated builtin(s) functionalities are deactivated)
#
# FUNCTIONAL PROGRAMMINGFUNDAMENTALS
# Solution
def reverse(lst):
    list1 = list()
    for elem in lst:
        list1.insert(0, elem)
    return list1