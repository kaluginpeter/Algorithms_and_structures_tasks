# Pyramid building in Egypt
# You are a Pharaoh in ancient Egypt, and you want to build the perfect pyramid for yourself. There's only a limited number of stones, however, and different kinds of stones vary in their value. You want to maximize the value of your pyramid while keeping it exactly three layers high.
#
# In essence, you're given an array of integers, which represent the stones, and your task is to assemble the highest-value pyramid from them. The pyramid is made out of exactly three layers, containing:
#
# Top layer: 1 integer
# Middle layer: 2 identical integers
# Bottom layer: 3 identical integers
# Additionally, no integer can appear in two or more layers. That is, each layer is made from stones of the same value, and stones of the same value can be used at most in one layer.
#
# Graphically, the structure of the pyramid looks like this, where
# 𝑥
# ≠
# 𝑦
# ≠
# 𝑧
# x
# 
# =y
# 
# =z
#
#     [z]
#   [y] [y]
#  [x][x][x]
# Input
# The input is an array that may contain positive and negative integers, as well as zeros. The integers are in no specific order and can be repeated. The array may also be empty.
#
# Output
# The output is a single integer – the sum of all integers that make up the pyramid. For example, given input [1,1,1,2,2,2,3,3,3], the highest-value pyramid is:
#
#     [1]
#   [2] [2]
#  [3][3][3]
# And the sum is thus:
# 3
# ⋅
# 3
# +
# 2
# ⋅
# 2
# +
# 1
# =
# 14
# 3⋅3+2⋅2+1=14.
#
# If it's not possible to build a pyramid from the given array (e.g. [-1,-1,0,0,1,1] or an empty one []), return None, null, or other language-specific alternative.
#
# Clarification
# Remember that there's no rule for descending or ascending order, so there's no restriction on placing the highest integer from the array on top of the pyramid.
#
# FUNDAMENTALS
# Solution
def pyramid(stones):
    storage: dict[int, int] = dict()
    for stone in stones:
        storage[stone] = storage.get(stone, 0) + 1
    available: list[int] = list(storage.keys())
    available.sort(key=lambda x: (x, storage[x]))
    third_idx: int = 0
    third: int = None
    for stone_idx in range(len(available)):
        if storage[available[stone_idx]] >= 3:
            if third is None or available[stone_idx] > third:
                third_idx, third = stone_idx, available[stone_idx]
    if third is None: return
    available.pop(third_idx)
    second_idx: int = 0
    second: int = None
    for stone_idx in range(len(available)):
        if storage[available[stone_idx]] >= 2:
            if second is None or second < available[stone_idx]:
                second_idx, second = stone_idx, available[stone_idx]
    if second is None: return
    available.pop(second_idx)
    if not available: return
    return 3 * third + 2 * second + max(available)