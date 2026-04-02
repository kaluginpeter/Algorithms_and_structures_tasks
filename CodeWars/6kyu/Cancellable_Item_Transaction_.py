# Overview
# 1. Transaction Log
#
# You're given a string of item transactions, for example:
#
# "2A3B4C1A2A"
# "5X6X1Y2Z1Y8X"
# Each transaction consists of a number followed by a letter, indicating the quantity of an item.
#
# For example, "4A" means 4 units of item A
#
# The string should be processed from left to right
#
# 2. Cancellation Rule
#
# Sometimes, a letter appears on its own. This means that the most recent transaction of that item is removed, if one exists.
#
# If there is no recent transaction for that item, the operation has no effect
#
# 3. Pricelist
#
# You're also given a pricelist (hashmap/dictionary), mapping each item to its unit price
#
# Task
# Your task is to calculate the total price using the transaction string and pricelist
#
# Constraints
# Multiple consecutive cancellations may occur
# Negative quantities will be tested
# Quantities with multiple digits will be tested
# Example
# price_dict = {"A":1,"B":3,"C":2}
# transaction = "1A2BA3AC4CA"
#
# Steps (processed from left to right):
#   - "1A" -> 1*1 = 1
#   - "2B" -> 2*3 = 6
#   -  "A" -> removes the most recent transaction of A (1A)
#   - "3A" -> 3*1 = 3
#   -  "C" -> no previous transaction of item C (nothing to remove)
#   - "4C" -> 4*2 = 8
#
#
#   Total: 17
# StringsParsing