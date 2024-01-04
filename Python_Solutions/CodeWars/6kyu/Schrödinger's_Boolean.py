# Can a value be both True and False?
#
# Define omnibool so that it returns True for the following:
#
# omnibool == True and omnibool == False
# If you enjoyed this kata, be sure to check out my other katas.
#
# LANGUAGE FEATURESMETAPROGRAMMINGPUZZLES
# Solution
class AlwaysTrue:
    def __eq__(self, other):
        return True

omnibool = AlwaysTrue()