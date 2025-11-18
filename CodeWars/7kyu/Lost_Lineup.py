# Developers were lined up at the coffee machine, but it broke! By the time they got to the backup one, they couldn't remember where people had been in the line. They want to restore the original order. The team lead, Carrol, was first. Everyone else remembers how many people had been standing between them and Carrol. Can you help them reconstruct the original order?
#
# Input: A list of n non-negative integers. Element i is the number of people that person i remembers being between them and Carrol.
#
# Output: A list of n non-negative integers, representing the original order. Since Carrol is first, there's no need for her to be included in the output.
#
# Example: Suppose input is [1, 2, 0]. This means there was one person between person 1 and Carrol, two people between person 2 and Carrol, and no people between person 3 and Carrol. Therefore the original order, excluding Carrol, must have been [3, 1, 2].
#
# Note: Since memories are fallible, people might misremember the number of people between them and Carrol. In this case there might be no solution, so return [ ].
#
# Example: Suppose input is [1, 0, 1]. Clearly it can't be the case that both person 1 and person 3 had one person between them and Carrol.
#
# Constraints: 1 ≤ n ≤ 100.
#
# Source: This kata is a modification of this problem from the practice competition of the International Collegiate Programming Competition, North America North Central region, 2025.
#
# Lists
# Solution
def find_lineup(distances):
    persons: list[int] = sorted([i for i in range(1, len(distances) + 1)], key=lambda person: distances[person - 1])
    distances.sort()
    for i in range(len(distances)):
        if i != distances[i]: return []
    return persons