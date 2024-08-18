# Alex is transitioning from website design to coding and wants to sharpen his skills with CodeWars.
# He can do ten kata in an hour, but when he makes a mistake, he must do pushups. These pushups really tire poor Alex out, so every time he does them they take twice as long. His first set of redemption pushups takes 5 minutes. Create a function, alexMistakes, that takes two arguments: the number of kata he needs to complete, and the time in minutes he has to complete them. Your function should return how many mistakes Alex can afford to make.
#
# FUNDAMENTALS
# Solution
def alex_mistakes(katas, time):
    c, t, s = 0, 5, time - katas * 6
    while s >= t:
        s -= t
        t *= 2
        c += 1
    return c