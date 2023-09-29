# You are given a sequence of a journey in London, UK. The sequence will contain bus numbers and TFL tube names as strings e.g.
#
# ['Northern', 'Central', 243, 1, 'Victoria']
# Journeys will always only contain a combination of tube names and bus numbers. Each tube journey costs £2.40 and each bus journey costs £1.50. If there are 2 or more adjacent bus journeys, the bus fare is capped for sets of two adjacent buses and calculated as one bus fare for each set.
#
# For example: 'Piccadilly', 56, 93, 243, 20, 14 -> "£6.90"
#
# Your task is to calculate the total cost of the journey and return the cost rounded to 2 decimal places in the format (where x is a number): £x.xx
#
# FUNDAMENTALS
# Solution
def london_city_hacker(journey):
    vehicle = "".join("t" if isinstance(k, str) else "b" for k in journey).replace("bb", "b")
    return f"£{sum(2.4 if i == 't' else 1.5 for i in vehicle):.2f}"