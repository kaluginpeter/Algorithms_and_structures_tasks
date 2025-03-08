# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said
#
# Description:
# Christmas is coming soon. Santa Claus is ready for the gift, he will give the gifts to the children. Of course, the gift of Santa Claus is not enough to give all the children, he needs to make a choice. Your task is to help Santa make the best choice:
#
# Suppose Santa Claus has n gifts, and each child has a wish (the number of gifts to be obtained). Provides an array of integers wishes representing all the wishes. Like this:
#
# n = 20
# wishes = [2,4,3,5,6,10,12,100]
# The result is a possible combination (an array) that happens to be able to distribute all of the gifts. In accordance with the above example, the results can be:
#
# [2,3,5,10] or [4,6,10] or [2,6,12] or...
# You should return one of them.
#
# If there is no valid result, return a string "Mission Failed!"
#
# Note:
# n and all elements of wishes always be positive integers.
# Some Examples
# distributeGifts(20,[2,4,3,5,6,10,12,100])
# Can return [2,3,5,10] or [4,6,10] or [2,6,12]...
#
# distributeGifts(20,[10,10,40,100])
# hould return [10,10]
#
# distributeGifts(20,[20,40,100])
# hould return [20]
#
# distributeGifts(20,[30,40,100])
# hould return "Mission Failed!"
# Puzzles
# Solution
def dfs(start: int, n: int, wishes: list[int], path: list[int]) -> bool:
    if n == 0: return True
    while start >= 0 and wishes[start] > n:
        start -= 1
    if start < 0: return False
    path.append(wishes[start])
    if dfs(start - 1, n - wishes[start], wishes, path): return True
    path.pop()
    return dfs(start - 1, n, wishes, path)

def distribute_gifts(n, wishes):
    wishes.sort()
    while wishes and wishes[-1] > n:
        wishes.pop()
    path: list[int] = []
    dfs(len(wishes) - 1, n, wishes, path)
    return path or 'Mission Failed!'