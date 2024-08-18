# You will be given a string (map) featuring a cat "C" and a mouse "m". The rest of the string will be made up of dots (".") The cat can move the given number of moves up, down, left or right, but not diagonally.
#
# You need to find out if the cat can catch the mouse from it's current position and return "Caught!" or "Escaped!" respectively.
#
# Finally, if one of two animals are not present, return "boring without two animals".
#
# Examples
# moves = 5
#
# map =
# ..C......
# .........
# ....m....
#
# returns "Caught!" because the cat can catch the mouse in 4 moves
# moves = 5
#
# map =
# .C.......
# .........
# ......m..
#
# returns "Escaped!" because the cat cannot catch the mouse in  5 moves
# GRAPH THEORYALGORITHMS
# Solution
def cat_mouse(map_, moves):
    if "C" not in map_ or "m" not in map_:
        return "boring without two animals"
    map_ =  map_.split('\n')
    for i in range(len(map_)):
        if "C" in map_[i]:
            cp, cr = map_[i].index("C") + 1, i + 1
        if "m" in map_[i]:
            mp, mr = map_[i].index("m") + 1, i + 1
    hunt_moves = abs(max(mr, cr) - min(mr, cr)) + abs(max(cp, mp) - min(cp, mp))
    return "Escaped!" if hunt_moves > moves else "Caught!"