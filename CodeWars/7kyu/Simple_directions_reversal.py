# In this Kata, you will be given directions and your task will be to find your way back.
#
# solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]) = ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
# solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr']) =  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']
# More examples in test cases.
#
# Good luck!
#
# Please also try Simple remove duplicates
#
# Algorithms
def solve(arr):
    if len(arr) <= 1: return arr
    path: list[str] = ['Begin ' + ' '.join(arr[-1].split()[1:])]
    prev: str = arr[-1].split()[0]
    if prev == 'Right': prev = 'Left'
    else: prev = 'Right'
    for i in range(len(arr) - 2, -1, -1):
        path.append(prev + ' ' + ' '.join(arr[i].split()[1:]))
        prev = arr[i].split()[0]
        if prev == 'Right': prev = 'Left'
        else: prev = 'Right'
    return path