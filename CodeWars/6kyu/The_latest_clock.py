# Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.
#
# The time should be in HH:MM format.
#
# Examples:
#
# digits: 1, 9, 8, 3 => result: "19:38"
# digits: 9, 1, 2, 5 => result: "21:59" (19:25 is also a valid time, but 21:59 is later)
# Notes
# Result should be a valid 24-hour time, between 00:00 and 23:59.
# Only inputs which have valid answers are tested.
# DATE TIMEFUNDAMENTALSALGORITHMS
# Solution
def latest_clock(*args):
    stock: list = list(args)
    mx: int = float('-inf')
    for i in range(len(stock)):
        for j in range(len(stock)):
            if i == j: continue
            for k in range(len(stock)):
                if k == j or k == i: continue
                for l in range(len(stock)):
                    if l == i or l == j or l == k: continue
                    x: int = stock[i] * 1000 + stock[j] * 100 + stock[k] * 10 + stock[l]
                    if ((stock[i]  == 2 and stock[j] < 4) or (stock[i] < 2 and stock[j] < 10)) and stock[k] < 6:
                        mx = max(mx, x)
    if mx == 0:
        return '00:00'
    if mx < 1000:
        if mx % 1000 > 2:
            return '0' + str(mx)[:1] + ':' + str(mx)[1:]
    return str(mx)[:2] + ':' + str(mx)[2:]