# Overview
# Elemental matchups are common in many RPGs, inluding the recent hit game Pikaman : Eracus' Legend.
#
# However, the game is still in alpha, and its elemental system is prone to change. This makes it difficult to determine the best elements to use against enemies.
#
# To solve this, you decide to write a program to compute an enemy's elemental matchups.
#
# Rules
# You're given two inputs:
# attack
#
# A hashmap of the form { str : tuple(list[str], list[str], list[str]) }
# Each element (key) is mapped to 3 lists:
# The first one contains elements that are weak to it
# The second contains elements that resist it
# The third contains elements that are immune to it
# enemy
#
# A list containing the enemy's element types (string)
# An enemy may possess multiple elements
# Elements interact through damage multipliers. All elements that appear anywhere in attack must be evaluated.
# Multipliers:
#
# Super effective -> x2
# Neutral (not listed in any of the lists) -> x1
# Not very effective -> x0.5
# No effect -> x0
# For each element being evaluated:
#
# The multiplier starts at x1
# For each element in enemy, determine its interaction type and apply the corresponding multiplier
# Multiply all applicable multipliers
# If any multiplier is x0, the final multiplier is x0
# For example:
# An enemy has elements Fire and Water
# Water is weak to grass (x2 multiplier), and fire resists grass (x0.5 multiplier)
# So the final multiplier for grass is x1 (neutral)
# Final multipliers are categorized as:
#
# Weakness -> Multiplier >= 2
# Neutral -> Multiplier = 1
# Resistance -> 0 < Multiplier < 1
# Immunity -> Multiplier = 0
# Task
# From the inputs, you must return three lists representing the enemy's weaknesses, resistances, and immunities.
#
# The elements in the lists must be sorted:
#
# By final multipliers in ascending order
# Alphabetically if the multipliers are equal
# Constraints
# 3 <= attack length <= 150
# Example
# 1. attack = {"Fire"    : (["Grass"], ["Water","Fire"], []),
#              "Water"   : (["Fire"], ["Grass","Water"], []),
#              "Grass"   : (["Water"], ["Fire","Grass"], [])}
#
#   enemy = ["Fire"]
#
#   Output = ["Water"], ["Grass","Fire"], []
#
#
#
# 2. attack : {"Fire"    : (["Grass","Air"], ["Water","Earth","Fire"], []),
#              "Water"   : (["Fire","Earth"], ["Grass","Thunder","Water"], []),
#              "Grass"   : (["Water","Earth"], ["Fire","Grass"], []),
#              "Thunder" : (["Water"], ["Grass","Thunder"], ["Earth"]),
#              "Earth"   : (["Fire","Thunder"], ["Grass"], ["Air"]),
#              "Air"     : (["Thunder","Grass"], ["Fire"], [])}
#
#   enemy = ["Grass", "Earth"]
#
#   Multipliers:
#
#     |  Elements  |  Grass  |  Earth  | Result |
#     ===========================================
#     |   Fire     |   x2    |  x0.5   |   x1   |
#     |  Water     |  x0.5   |   x2    |   x1   |
#     |  Grass     |  x0.5   |   x2    |   x1   |
#     |  Thunder   |  x0.5   |   x0    |   x0   |
#     |   Air      |   x2    |   x1    |   x2   |
#     |  Earth     |  x0.5   |   x1    |  x0.5  |
#     ===========================================
#
#
#   Weaknesses = Air
#   Resistances = Earth
#   Immunities = Thunder
#
#   Output = ["Air"], ["Earth"], ["Thunder"]
#
#
#
# 3. attack = same as 2
#    enemy = ["Water", "Thunder", "Earth"]
#
#    Multipliers :
#    |  Elements  |  Water  |  Earth  |  Thunder  |  Result  |
#    =========================================================
#    |   Fire     |  x0.5   |  x0.5   |    x1     |   x0.25  |
#    |   Water    |  x0.5   |   x2    |   x0.5    |   x0.5   |
#    |   Grass    |   x2    |   x2    |    x1     |    x4    |
#    |  Thunder   |   x2    |   x0    |   x0.5    |    x0    |
#    |    Air     |   x1    |   x1    |    x2     |    x2    |
#    |   Earth    |   x1    |   x1    |    x2     |    x2    |
#    =========================================================
#
#    Weaknesses = Air(x2), Earth(x2), Grass(x4)
#    Resistances = Fire(x0.25), Water(x0.5)
#    Immunities = Thunder
#
#    Output = ["Air","Earth","Grass"], ["Fire","Water"], ["Thunder"]
# AlgorithmsLogicSorting