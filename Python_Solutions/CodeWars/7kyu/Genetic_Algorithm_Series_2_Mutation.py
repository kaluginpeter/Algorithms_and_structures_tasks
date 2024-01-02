# Mutation is a genetic operator used to maintain genetic diversity from one generation of a population of genetic algorithm chromosomes to the next.
#
# Mutation
#
# A mutation here may happen on zero or more positions in a chromosome. It is going to check every position and by a given probability it will decide if a mutation will occur.
#
# A mutation is the change from 0 to 1 or from 1 to 0.
#
# Note: Some tests are random. If you think your algorithm is correct but the result fails, trying again should work.
#
# See other katas from this series
# Genetic Algorithm Series - #1 Generate
# Genetic Algorithm Series - #2 Mutation
# Genetic Algorithm Series - #3 Crossover
# Genetic Algorithm Series - #4 Get population and fitnesses
# Genetic Algorithm Series - #5 Roulette wheel selection
# ALGORITHMSGENETIC ALGORITHMSSTRINGS
# Solution
from random import choices
def mutate(chromosome, p):
    return ''.join(choices([str(int(not bool(int(i)))), i], [p, 1 - p])[0] for i in chromosome)