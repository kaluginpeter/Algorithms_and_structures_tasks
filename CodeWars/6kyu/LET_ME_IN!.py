# Prologue:
# You get back from work late at night, roaming the streets of Japan (it has to be!). As you are headed home, starved after a long and grueling day at work, stumble upon a ramen shop still serving customers. You dash in, practically drooling for some ramen -- but as soon as you walk in, you realize just how chaotic this restaurant is.
#
# Problem:
# You're standing in a line, where everybody seems to be playing a game for entry. The owner of the restaurant stands at the "front", bringing guests in individually.
#
# There are four "types" of guests:
#
# Known guests -> Guests who know the restaurant owner personally. These people can enter as they please, without having to wait in a line. Whenever the owner meets a known guest, he yells out "SWAP", requiring everybody to switch places with the person on the "opposite" end of the line, except for other known guests
# Members → Guests who have an active membership subscription at the food chain. These people have priority over unknown guests, but are not immune to swapping.
# Decoys → These are actually staff members that are hidden into the line, in order to make the game more interesting. When swapping, decoys aren’t allowed to swap, maintaining their position in line. To better disguise themselves, they are given the same priority level as "unknown guests".
# Unknown Guests → The typical person, either too broke to afford a membership, or trying out the restaurant for the first time. They are subject to swaps and get bottom tier priority.
# You are given a list of the people that are waiting in queue, each numbered 1-3 except you, who is 0, and "unknown guests", which can be any other positive number. Your goal is to determine how long it will take for you to get seated (with each person being removed from queue being considered a "minute", including yourself).
#
# Examples:
# queue = [1, 1, 3, 2, 0] # The given queue
# sorted = [1, 1, 2, 3, 0] # Sorted by priority
# #                     ^-- you
# The 1's are the "known guests", so they get priority.
# The 2's are the "members", so they get secondary priority.
# The resulting array is [1, 1, 2, 3, 0]
# The first "known guest" gets consumed, so the swap occurs on the remaining elements in the list [1, 2, 3, 0]
# 1 cannot swap with 0, and 3 cannot swap with 2
# Repeat, resulting in [2, 3, 0].
# 0 and 2 can be swapped, resulting in [0, 3, 2]
# With 0 in front, it took 3 minutes for you to get seated, so the answer is 3
# queue = [0, 8, 2, 1, 4, 2, 12, 3, 2] # The given queue
# sorted = [1, 2, 2, 2, 0, 8, 4, 12, 3] # Sorted by priority
# #                     ^-- you
# The first "known guest" gets consumed: [2, 2, 2, 0, 8, 4, 12, 3]
# 2 cannot swap with 3
# the rest swap, resulting in: [2, 12, 4, 8, 0, 2, 2, 3]
# The numbers up to the 0 get "consumed", as no more swapping is required
# With 0 in front, it took 6 minutes for you to get seated, so the answer is 6
# FUNDAMENTALSPERFORMANCE
# Solution
from itertools import count
def get_in_line(l):
    l.sort(key=lambda x: x if 0 < x < 3 else 3)
    for n in count(1):
        x = l.pop(0)
        if x == 0:
            return n
        elif x == 1:
            for i in range(len(l)//2):
                j = len(l) - 1 - i
                if l[i] not in (1,3) and l[j] not in (1,3):
                    l[i], l[j] = l[j], l[i]