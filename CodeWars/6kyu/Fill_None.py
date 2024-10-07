# Task
# Write a function that accepts a list that can contain missing data, and an integer representing the method on how to fill the missing data if there is any. Missing data is represented as None. The list will only contain integers and None values.
#
# Note that depending on the language you attempt this kata with, None corresponds to:
#
# None (Python)
# undefined (Javascript)
# Nothing (Haskell)
# The fill method rules are outlined below:
#
# Fill method:
#   -1: backwards
#    0: nearest
#    1: forwards
# Example
# arr = [None, 1, None, None, None, 2, None]
#
# fill(arr, -1) == [1, 1, 2, 2, 2, 2, None]  # None replaced by closest int on the right
# fill(arr,  0) == [1, 1, 1, 1, 2, 2, 2]     # None replaced by closest int. If equidistant, choose the smallest int
# fill(arr,  1) == [None, 1, 1, 1, 1, 2, 2]  # None replaced by closest int on the left
# Notes
# [] should return []
# [None] should return [None]
# Arrays will only contain integers and None values
# FUNDAMENTALS
# Solution
def get_right_bound(target: int, sources: list[int]) -> int:
    for idx in sources:
        if idx > target: return idx
    return -1


def get_left_bound(target: int, sources: list[int]) -> int:
    for idx in sources[::-1]:
        if idx < target: return idx
    return -1


def fill(arr, method=0):
    if method != 0:
        for idx in range(len(arr)):
            if arr[idx] is None:
                if method == -1:
                    arr[idx] = arr[min(idx + 1, len(arr) - 1)]
                else: arr[idx] = arr[max(idx - 1, 0)]
        for idx in range(len(arr) - 1, -1, -1):
            if arr[idx] is None:
                if method == -1:
                    arr[idx] = arr[min(idx + 1, len(arr) - 1)]
                else: arr[idx] = arr[max(idx - 1, 0)]
        return arr
    storage: list[int] = [idx for idx in range(len(arr)) if arr[idx] is not None]
    for idx in range(len(arr)):
        if arr[idx] is None:
            right_part: int = get_right_bound(idx, storage)
            left_part: int = get_left_bound(idx, storage)
            if right_part == left_part == -1: continue
            elif right_part == -1: right_part = left_part
            elif left_part == -1: left_part = right_part
            if idx - left_part == right_part - idx:
                arr[idx] = min(arr[left_part], arr[right_part])
            else:
                arr[idx] = arr[[left_part, right_part][idx - left_part > right_part - idx]]
    return arr