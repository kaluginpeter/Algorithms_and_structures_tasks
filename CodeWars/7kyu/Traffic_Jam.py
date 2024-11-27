# Description
# A series of cars are lined up at a traffic light, each with a different speed. Given the duration of the green light, calculate the minimum number of green light cycles required for all the cars to pass through the traffic light.
#
# Rules
# Cars wait in line one after another, and cross the intersection in the order they are queued, starting from the right hand side of the list.
#
# Multiple cars can pass during one green light cycle, as long as the total time does not exceed the green light duration.
#
# Each green light cycle starts with the remaining cars, and the process repeats until no cars remain.
#
# Input / Output
# Your function will receive:
#
# A list of integers - the time it takes for each car to pass the traffic light
#
# The time taken will always be greater than 0
#
# This vehicle list will not be empty
#
# An integer - the duration of the green light
#
# The duration of the green light is always greater than or equal to the travel time of each individual vehicle
# Your function should return:
#
# An integer - the number of green light cycles needed for all the cars to pass through
# Example
# ([15, 2, 8, 7], 16) -> answer: 3
#
# The first two cars (with a speed of 7 and 8 respectively) have time to pass the traffic light together (as 7 + 8 = 15, which is less than the duration of the green light).
#
# Then, the car with a speed of 2 is able to pass, but the next car which has a speed of 15 is not able to pass, and has to wait for one more cycle.
#
# Output: 3 (Minimum of 3 green light cycles required)
# FundamentalsStringsAlgorithms