# Farmer Bob have a big farm, where he growths chickens, rabbits and cows. It is very difficult to count the number of animals for each type manually, so he diceded to buy a system to do it. But he bought a cheap system that can count only total number of heads, total number of legs and total number of horns of animals on the farm. Help Bob to figure out how many chickens, rabbits and cows does he have?
#
# All chickens have 2 legs, 1 head and no horns; all rabbits have 4 legs, 1 head and no horns; all cows have 4 legs, 1 head and 2 horns.
#
# Your task is to write a function
#
# , which returns a dictionary
#
# {"rabbits" : rabbits_count, "chickens" : chickens_count, "cows" : cows_count}
# Parameters legs_number, heads_number, horns_number are integer, all tests have valid input.
#
# Example:
#
# get_animals_count(34, 11, 6); # Should return {"rabbits" : 3, "chickens" : 5, "cows" : 3}
# get_animals_count(154, 42, 10); # Should return {"rabbits" : 30, "chickens" : 7, "cows" : 5}
# FUNDAMENTALSALGORITHMSMATHEMATICS