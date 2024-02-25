# Implement a function which behaves like the 'uniq -c' command in UNIX.
#
# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance together with the number of times a duplicate elements occurred in the original array.
#
# Example:
# ['a','a','b','b','c','a','b','c'] --> [('a',2),('b',2),('c',1),('a',1),('b',1),('c',1)]
# ARRAYSALGORITHMS
# Solution OnePass O(N) O(N)
def uniq_c(seq):
    ans: list = list()
    count: int = 0
    start: bool = True
    object = None
    for i in seq:
        if start:
            start = False
            object = i
            count += 1
        elif i != object:
            ans.append((object, count))
            object, count = i, 1
        else:
            count += 1
    if not start:
        ans.append((object, count))
    return ans