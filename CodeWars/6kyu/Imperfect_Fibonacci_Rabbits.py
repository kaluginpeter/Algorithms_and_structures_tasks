# Background
# This is an extension of this kata so I suggest you complete that one first.
#
# Imperfect Rabbits
# In this kata, our rabbits are sadly imperfect, they only live for a few months, and then they die! As in the previous kata however, our rabbits:
#
# Take one month to mature.
# Always birth equal numbers of male and female offspring.
# Never have to compete for resources.
# Have no predators.
# At the start of the first month you start with one pair of immature rabbits.
#
# Kata
# In this kata you must implement the method provided to you with arguments n, b, l, where:
#
# n is the number of the months to simulate,
# b is the number of pairs each adult pair gives birth to, and,
# l is the lifespan in months of a rabbit.
# Examples
# n = 6, b = 3, l = 6
# return 96
#
# n = 8, b = 3, l = 4
# return 423
# Algorithms
def imperfect_fib_rabbits(n, b, l):
    rabbits_by_age = [0] * (l)
    rabbits_by_age[0] = 1

    for month in range(n):
        new_borns = 0

        for age in range(1, l):
            new_borns += rabbits_by_age[age] * b

        for age in range(l - 1, 0, -1):
            rabbits_by_age[age] = rabbits_by_age[age - 1]

        rabbits_by_age[0] = new_borns
    total_rabbits = sum(rabbits_by_age)
    return total_rabbits