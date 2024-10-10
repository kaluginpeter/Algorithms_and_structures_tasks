# The longest street in the world, MAX_STREET, is crossed by many other streets and driven by many drivers. Determine how many streets each driver crosses.
#
# Inputs
# (1) A list (or array, depending on language) of streets that intersect MAX_STREET. (2) A list (or array, depending on language) of drivers. Each driver is represented by a pair of streets. The first element of the pair is the street where they enter MAX_STREET; the second is the street they exit. The driver crosses all the streets between those two streets.
#
# Output
# A list (or array, depending on language) showing how many streets each driver crosses.
#
# Example
# count_streets(["first", "second", "third", "fourth", "fifth", "sixth", "seventh"],
#                [("first", "second"), ("second", "seventh"), ("sixth", "fourth")]) should return [0,4,1].
#
# Details:
# (1) Each street name is a non-empty word of no more than 10 letters. There are no duplicate street names.
#
# (2) The entry and exit streets for each driver are distinct. They are guaranteed to come from the list of streets.
#
# (3) The number of streets n satisfies 2 ≤ n ≤ 105. The number of drivers d satisfies 1 ≤ d ≤ 105. So efficiency is important.
#
# Source: International Collegiate Programming Contest, North Central North American Regional, 2022.
#
# ARRAYSSEARCHINGPERFORMANCE
# Solution
def count_streets(streets, drivers):
    output: list[int] = []
    storage: dict[str, int] = dict()
    distance: int = 1
    for street in streets:
        storage[street] = distance
        distance += 1
    for start, end in drivers:
        start_d: int = storage[start]
        end_d: int = storage[end]
        output.append(max(start_d, end_d) - min(start_d, end_d) - 1)
    return output