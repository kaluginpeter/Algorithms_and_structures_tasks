# In genetic algorithms, crossover is a genetic operator used to vary the programming of chromosomes from one generation to the next.
#
# The one-point crossover consists in swapping one's cromosome part with another in a specific given point. The image bellow shows the crossover being applied on chromosomes 1011011001111 and 1011100100110 with the cut point (index) 4:
#
#
#
# In this kata you have to implement a function crossover that receives two chromosomes chromosome1, chromosome2 and a zero-based index and it has to return an array with the crossover result on both chromosomes [chromosome1, chromosome2].
#
# Example:
# crossover('111000', '000110', 3) should return ['111110', 000000']
#
# See other katas from this series
# Genetic Algorithm Series - #1 Generate
# Genetic Algorithm Series - #2 Mutation
# Genetic Algorithm Series - #3 Crossover
# Genetic Algorithm Series - #4 Get population and fitnesses
# Genetic Algorithm Series - #5 Roulette wheel selection
# This kata is a piece of2 kyuBinary Genetic Algorithm
#
# STRINGSALGORITHMSGENETIC ALGORITHMS
# Solution
def crossover(chromosome1, chromosome2, index):
    x, y = '', ''
    for i in range(index, len(chromosome1)):
        x += chromosome2[i]
        y += chromosome1[i]
    return [chromosome1[:index] + x, chromosome2[:index] + y]