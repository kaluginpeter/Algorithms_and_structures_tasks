# Unique Sets
# Task:
#
# You are given a list of sets. Each set contains multiple hashable values which can be either simple (e.g., integers, strings) or compound. For the purpose of this task (and in the Python tests), compound values are limited to tuples and frozensets. Compound values may also include nested compound values, and every individual element at any level of nesting must be considered when checking for uniqueness.
#
# Your goal is to determine whether all sets in the list are unique according to the following rules:
#
# No Overlap Across Sets: No value (whether directly in a set or nested within a compound structure) should appear in more than one set. For example, if the number 1 appears as an element in one set and also inside a tuple in another set, this violates uniqueness.
#
# No Duplicates Within a Set: A set is considered non-unique if any value appears more than once within that set—even if one occurrence is nested within a compound structure. For instance, if the value 5 appears both directly and inside a nested tuple within the same set, that set is not unique.
#
# Empty Input: If the input list is empty, return True, as there are no sets to conflict with each other.
#
# Input:
#
# An array (list) of sets.
# Set Contents: Each set contains one or more hashable values. These values can be:
# Simple values: integers or strings.
# Compound values(in Python): Tuples and frozensets only. These values may themselves contain nested compound values.
# Examples:
#
# [ {5,8 , (1,2), "rvbc" }, {"fnyh", "esa", 1}, {("cev","cdv",0), 18}   ] -> False
#
# [ {5,8 , (1,2), "rvbc" }, {"fnyh", "esa", 6}, {("cev","cdv",0), 18}   ] -> True
#
# [] -> True
#
# [ {5,8 , (1,2), "rvbc" }, { {"fnyh", 0}, "esa", 6}, {("cev","cdv",0), 18}   ] -> False
#
# [ {5,8 , (1,(2,6,(9,100,107),890,(1,(5,6))), (3,4,5)), "rvbc" }, {"fnyh", "esa", 6}, {("cev","cdv",20), 18}   ] -> False ( Since "1","6" and "5" appear twice)
#
# ListsArraysSets
# Solution
g: set = set()
def check_unique(arr, level: int = 0):
    if not arr: return True
    if level == 0: g.clear()
    for i in arr:
        if isinstance(i, tuple) or isinstance(i, frozenset) or isinstance(i, set):
            if not check_unique(i, level+1): return False
        elif i in g: return False
        else: g.add(i)
    return True