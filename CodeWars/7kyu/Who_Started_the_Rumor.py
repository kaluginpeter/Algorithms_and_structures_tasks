# Overview
# Recently, there has been a rumor spreading, and you want to find who started it.
#
# You begin questioning people involved in the rumor. Unfortunately, nobody is willing to tell you who they got the rumor from. However, they won't hesitate to tell you who they passed the rumor to.
#
# This information is stored as a record (hashmap), where each person (string) is mapped to the people they told the rumor to (list of strings).
#
# Task
# Given the input record, determine who started the rumor using only the available information.
#
# Everyone involved in the rumor is guaranteed to appear in the record, either as a key or within a value list.
#
# Return the result as a list.
#
# Note
# It is guaranteed to have at least 1 culprit
# If there are multiple culprits, they must be sorted alphabetically.
# Example
# 1. record = {"Sarah": ["Elle"], "Larry":["Sarah","Elle"], "John":["Larry","May"],
#             "May":["Sarah"], "Elle":["May"]}
#   Output: ["John"]
#
#
# 2. record = {"Mike":["Paige","Rose"], "Paige":["Hugh"], "Liam":["Rose"],
#              "Rose":["Paige", "Hugh"], "Hugh":["Liam"], "Victor":["Rose","Liam"]}
#   Output: ["Mike","Victor"]
# Fundamentals
# Solution
def rumor_starter(record):
    receivers = set()
    for people in record.values(): receivers.update(people)
    return sorted([
        person for person in record
        if person not in receivers
    ])