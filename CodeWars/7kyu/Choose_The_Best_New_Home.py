# Choose The Best New Home
# Overview
# You are looking for the perfect place to move into! You have a list of available housing locations, a dictionary of your dream preferences, and a prioritized ranking list. Your task is to calculate the match score for each home and return the name of the absolute best match.
#
# Inputs
# places (dict): A collection of available homes. Each home is a dictionary containing various traits (e.g., {"type": "apartment", "ghosts": "none"}).
# preferences (dict): Your ideal values for those traits (e.g., {"type": "apartment", "ghosts": "friendly_casper"}).
# priorities (list): A list of trait names ordered from most important to least important.
# Scoring Rules
# Points are awarded based on the position of a matching trait inside the priorities list:
#
# The 1st item in your priorities list is worth 6 points if the home's trait matches your preference.
# The 2nd item is worth 5 points, the 3rd is worth 4 points, down to the 6th item which is worth 1 point.
# Any trait present in a home or preference that is not listed in the priorities array scores 0 points. Missing or mismatched traits also score 0 points.
# Tie-Breaker Rule
# If two or more homes achieve the exact same highest score, return the home name that comes first alphabetically (e.g., "MansionA" beats "MansionB"). If there is a tie at 0 points, the alphabetical rule still applies!
#
# Step-by-Step Example
# places = {
#     "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
#     "House_B":     {"type": "house",     "cats": "many_cats_to_pet"}
# }
# preferences = {"type": "apartment", "cats": "many_cats_to_pet"}
# priorities = ["type", "cats"]
#
# # --- Scoring Apartment_A ---
# # 'type' is 1st in priorities (6 pts). Apartment_A has 'apartment' (Matches preference!) -> +6 pts
# # 'cats' is 2nd in priorities (5 pts). Apartment_A has 'zero_cats' (Mismatches 'many_cats_to_pet') -> +0 pts
# # Total Score = 6
#
# # --- Scoring House_B ---
# # 'type' (6 pts). House_B has 'house' (Mismatches 'apartment') -> +0 pts
# # 'cats' (5 pts). House_B has 'many_cats_to_pet' (Matches preference!) -> +5 pts
# # Total Score = 5
#
# # Winner: "Apartment_A"
# Write a function choose_best_home(places, preferences, priorities) that computes the top destination!
#
# FundamentalsListsAlgorithms
# Solution
def choose_best_home(places, preferences, priorities):
    weights = {
        trait: len(priorities) - i
        for i, trait in enumerate(priorities)
    }
    best_name = min(places)
    best_score = -1
    for name in places:
        score = 0
        home = places[name]
        for trait, pref in preferences.items():
            if home.get(trait) == pref: score += weights.get(trait, 0)
        if score > best_score:
            best_score = score
            best_name = name
        elif score == best_score and name < best_name: best_name = name
    return best_name