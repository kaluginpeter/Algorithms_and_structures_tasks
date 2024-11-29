# The pizza store wants to know how long each order will take. They know:
#
# Prepping a pizza takes 3 mins
# Cook a pizza takes 10 mins
# Every salad takes 3 mins to make
# Every appetizer takes 5 mins to make
# There are 2 pizza ovens
# 5 pizzas can fit in a oven
# Prepping for a pizza must be done before it can be put in the oven
# There are two pizza chefs and one chef for appitizers and salads combined
# The two pizza chefs can work on the same pizza
# Write a function, order, which will tell the company how much time the order will take.
#
# See example tests for details.
#
# Puzzles
# Solution
def order(pizzas, salads, appetizers):
    garnire_time: float = salads * 3 + appetizers * 5 # for salads and appetizers
    pizza_time = pizzas * 3 / 2 # for prepping pizzas
    parts_ovens: int = pizzas // 5 + int(pizzas % 5 != 0)  # total ovens needed
    pizza_time += parts_ovens // 2 * 10 + parts_ovens % 2 * 10 # total bake time
    return max(pizza_time, garnire_time)