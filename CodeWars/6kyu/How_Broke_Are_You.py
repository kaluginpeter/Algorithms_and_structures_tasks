# You are tracking your "broke level" based on daily expenditures.
#
# A broke event is counted under the following conditions:
#
# If a single day's expenditure is less than or equal to 3 dollars.
# If daily expenditure is less than or equal to 7 dollars for 3 consecutive days.
# If daily expenditure is less than or equal to 10 dollars for 7 consecutive days.
# Important:
#
# A broke event can either be a day long, 3 days or 7 days long. Otherwise a new broke event is started.
# If a smaller threshold event occurs inside a larger qualifying streak, it does NOT count separately.
# Overlapping streaks count as a single broke event. eg, [7,3,7] would only be one broke event
# Example: [5,6,7,20,3] returns 2, ie 5,6,7 and 3
#
# Given a list of daily expenditures, return the total number of broke events.
#
# ArraysAlgorithmsLogic