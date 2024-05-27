# You work at a taxi central.
# People contact you to order a taxi. They inform you of the time they want to be picked up and dropped off.
#
# A taxi is available to handle a new customer 1 time unit after it has dropped off a previous customer.
#
# What is the minimum number of taxis you need to service all requests?
#
# Constraints:
# Let N be the number of customer requests:
# N is an integer in the range [1, 100k]
# All times will be integers in range [1, 10k]
# Let PU be the time of pickup and DO be the time of dropoff
# Then for each request: PU < DO
# The input list is NOT sorted.
# Examples:
# # Two customers, overlapping schedule. Two taxis needed.
# # First customer wants to be picked up 1 and dropped off 4.
# # Second customer wants to be picked up 2 and dropped off 6.
# requests = [(1, 4), (2, 6)]
# min_num_taxis(requests) # => 2
#
# # Two customers, no overlap in schedule. Only one taxi needed.
# # First customer wants to be picked up 1 and dropped off 4.
# # Second customer wants to be picked up 5 and dropped off 9.
# requests = [(1, 4), (5, 9)]
# min_num_taxis(requests) # => 1
# DATA STRUCTURESALGORITHMSPRIORITY QUEUESSCHEDULING
# Solution
import heapq

def min_num_taxis(requests):
    requests = sorted(enumerate(requests), key=lambda x: (x[1][0], x[1][1]))
    heap = []
    room_count = 0
    for original_index, (arrival, departure) in requests:
        if heap and heap[0][0] < arrival:
            earliest_departure, assigned_room = heapq.heappop(heap)
            heapq.heappush(heap, (departure, assigned_room))
        else:
            room_count += 1
            assigned_room = room_count
            heapq.heappush(heap, (departure, assigned_room))
    return room_count