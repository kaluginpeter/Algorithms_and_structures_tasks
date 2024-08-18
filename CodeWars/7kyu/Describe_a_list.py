# Write function describeList which returns "empty" if the list is empty or "singleton" if it contains only one element or "longer"" if more.
#
# LISTSFUNDAMENTALS
# Solution
def describeList(list):
    return 'singleton' if len(list) == 1 else 'longer' if len(list) > 1 else 'empty'