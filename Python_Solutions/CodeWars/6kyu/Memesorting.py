# Roma is programmer and he likes memes about IT,
# Maxim is chemist and he likes memes about chemistry,
# Danik is designer and he likes memes about design,
# and Vlad likes all other memes.
#
# You will be given a meme (string), and your task is to identify its category, and send it to the right receiver: IT - 'Roma', chemistry - 'Maxim', design - 'Danik', or other - 'Vlad'.
#
# IT meme has letters b, u, g.
# Chemistry meme has letters b, o, o, m.
# Design meme has letters e, d, i, t, s.
# If there is more than 1 possible answer, the earliest match should be chosen.
#
# Note: letters are case-insensetive and should come in the order specified above.
#
# Examples:
# (Matching letters are surrounded by curly braces for readability.)
#
# this is programmer meme {b}ecause it has b{ug}
# this is also program{bu}r meme {g}ecause it has needed key word
# this is {ed}s{i}gner meme cause i{t} ha{s} key word
#
# this could {b}e chemistry meme b{u}t our{g}Gey word 'boom' is too late
#     instead of
# this could {b}e chemistry meme but {o}ur gey w{o}rd 'boo{m}' is too late
# STRINGSREGULAR EXPRESSIONSFUNDAMENTALSSORTING
# Solution
def memesorting(meme):
    it: list[str] = ['b', 'u', 'g']
    x, y, z = 0, 0, 0
    ht: dict[int, str] = {'Roma': x, 'Maxim': y, 'Danik': z}
    chemistry: list[str] = ['b', 'o', 'o', 'm']
    design: list[str] = ['e', 'd', 'i', 't', 's']
    for i in range(len(meme)):
        if meme[i].lower() == it[0]:
            it.pop(0)
            x += 1
        if meme[i].lower() == chemistry[0]:
            chemistry.pop(0)
            y += i
        if meme[i].lower() == design[0]:
            design.pop(0)
            z += i
        ht = {'Roma': x, 'Maxim': y, 'Danik': z}
        stack: list[int] = [[x, y, z][i] for i in range(3) if not [it, chemistry, design][i]]
        if stack:
            return [k for k, v in ht.items() if v == min(stack)][0]
    return 'Vlad'