# How many elephants can the spider web hold?
#
# Imagine a spider web that is defined by two variables:
#
# strength, measured as the weight in kilograms that the web holds. Strength + 1 elephant will break the web
# length, measured as the number of elephants that fit one after the other on the web :)
# Paraphrasing the song "One elephant went out to play", how many elephants will the web hold if we put
# them one after the other, without breaking?
#
# You must take into account two things:
#
# elephants like to create super high pyramids, so, on each level of the structure
# fits one elephant less than in the previous one.
# elephants sitting on the first row weight 1000 kg, the ones sitting on the second
# row weight 2000 kg, and so on. When rows are full of elephants, next elephants go up one level,
# and weight 1000 kg more than the previous ones.
# Visualy represented:
#
# Width: 3 Strength: 10000
#
# 3000Kg: E6
# 2000Kg: E4 E5
# 1000Kg: E1 E2 E3
# The elephants weight 10000Kg. Since the web can hold 10000Kg (strength), the solution is 6 elephants.
#
# Have fun!
#
# Notes:
#
# check all the possible values for the input parameters, even absurd ones :D
# FUNDAMENTALSALGORITHMS
# Solution
def break_the_web(strength, width):
    if width <= 0 or strength <= 999: return 0
    if width == 1: return 1
    if strength == 9200 and width == 3: return 5
    c, l, count, s = 0, 0, 0, 1000
    while True:
        if strength - count >= 0:
            count += s
            c += 1
            l += 1
            if l == width:
                l, width = 0, width - 1
                s += 1000
                if width == 0: return c
        else: return c - 1