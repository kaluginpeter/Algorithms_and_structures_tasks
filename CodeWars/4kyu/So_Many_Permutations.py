# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
#
# Create as many "shufflings" as you can!
#
# Examples:
#
# With input 'a':
# Your function should return: ['a']
#
# With input 'ab':
# Your function should return ['ab', 'ba']
#
# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']
#
# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# Note: The order of the permutations doesn't matter.
#
# Good luck!
#
# PERMUTATIONSSTRINGSALGORITHMS
# Solution
def permutations(s):
    l = []
    def permute(data, i, length):
        if i == length:
            l.append(''.join(data) )
        else:
            for j in range(i, length):
                data[i], data[j] = data[j], data[i]
                permute(data, i + 1, length)
                data[i], data[j] = data[j], data[i]
    permute(list(s), 0, len(s))
    return set(l)