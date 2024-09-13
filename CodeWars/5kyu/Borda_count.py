# You have to choose a collective solution using the Borda method. According to this method, the voting results are expressed in terms of the number of points scored by each of the candidates. So, in an election of n candidates, each voter ranks all candidates strictly in descending order of preference, for the first place according to preference n - 1 points are awarded to the candidate, n - 2 points for the second place, etc. (for the last place - 0 points). All points scored by each candidate are summed up. Then candidates with fewer points than the arithmetic mean are removed, and the method is repeated until there are only candidates with the same results or a candidate left.
#
# More information on Wikipedia
#
# For example there are 3 people with different preferences:
#
#   Maria:           Alexey:               Vladimir:
#       Coffee            Hot Chocolate         Coffee
#       Tea               Tea                   Hot Chocolate
#       Hot Chocolate     Coffee                Tea
#   Drink:    Score:
#   Coffee    (2 + 2 + 0) = 4
#   Tea       (1 + 1 + 0) = 2
#   Chocolate (2 + 1 + 0) = 3
#
#   Mean      (4 + 2 + 3) / 3 = 3
# So we exclude tea as 2 < 3, and the preference table takes the following form:
#
#   Maria           Alexey            Vladimir
#     Coffee          Hot Chocolate     Coffee
#     Hot Chocolate   Coffee            Hot Chocolate
# Next:
#
#   Drink:        Score:
#   Coffee        (1 + 0 + 1) = 2
#   Hot Chocolate (0 + 1 + 0) = 1
#
#   Mean           1.5
# Now we exclude hot chocolate (1 < 1.5) and we are done. Our collective solution is coffee.
#
# Input (dictionary):
#
# {'A': ['a', 'b', 'c'], 'B': ['b', 'c', 'a']}
#
# Output (set):
#
# {'a', 'b'}
#
# ALGORITHMS
# Solution
def borda_count(table):
    while True:
        products: dict[str, int] = dict()
        for person in table:
            priority: int = len(table[person]) - 1
            for vote in table[person]:
                products[vote] = products.get(vote, 0) + priority
                priority -= 1
        mean: float = sum(products.values()) / len(products)
        is_change: bool = False
        for product in products:
            if products[product] < mean:
                for people in table:
                    table[people].remove(product)
                    is_change = True
        if not is_change: return products.keys()