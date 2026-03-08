# This kata is inspired by the arcade puzzle game Super Puzzle Fighter II Turbo (seen above).
#
# In the game Super Puzzle Fighter II Turbo, the player controls pairs of blocks (referred to as "Gems") that drop into a pit-like playfield.
#
# In this kata, your objective is to write a function that, given a sequence of Gem pairs and movement instructions, will return the ending game state.
#
# Game Mechanics
# gems1
#
# The playfield is a matrix with 12 rows and 6 columns; it begins empty.
# Gems come in four different colors — red, blue, green, and yellow.
# Similar in style to other tile-matching video games, a pair of adjacent Gems will descend into the playfield. This pair can be moved left and right, and can be rotated clockwise and counter-clockwise. Once it lands onto an obstacle, the process repeats.
# If the pair lands on an obstacle, but one of the Gems has empty space below it, the pair will disjoint and the unsupported Gem will continue to descend until it lands onto an obstacle.
# In the image above (left), the green-blue Gem pair inside the white rectangular outline will disjoint, with the green Gem merging with the green Power Gem and the blue Gem landing on the yellow Gem, if allowed to drop straight down as is.
# Power Gems: Adjacent clusters of same-colored Gems in rectangular shapes, that are 2 x 2 or greater in width and height, will merge into one larger solid Gem, known as a Power Gem. In the image above (left), the larger blue Gem located at the bottom left is a 4 x 4 Power Gem. The green Gem just above it is a 2 x 3 Power Gem. In the image to the right, the green Gem that falls merges with the green Power Gem, transforming it into a 2 x 4 Power Gem.
# Each Gem pair descends from the Drop Alley, which is the top of the fourth column from the left, as shown above with the Gem pair inside the white dashed rectangle.
# Crash Gems are special Gems that, upon contact with a same-colored Gem, will destroy all connected Gems of the same color, including other Crash Gems of the same color. In the process, the Crash Gem will self-destruct.
# In the image above (left), a yellow Crash Gem (the yellow circle) is part of a descending Gem pair. If left to fall straight down as is, it will destroy all the connected yellow Gems, resulting in the image to the right. The blue Crash Gem remains until a blue Gem comes in contact with it.
# Rainbow Gems are a rare type of special Gem that destroy all Gems that match the color of the Gem it lands on, while self-destructing in the process. If it lands on the floor of the playfield, no other Gems will be destroyed.
# When rotating a Gem pair, the 2nd Gem will rotate around the 1st Gem. In the image above (left), the yellow Crash Gem will rotate around the red Gem. Note that a rotation may cause a shift in lateral position if a Gem pair is touching the left or right wall (to keep the Gems within the boundaries of the playfield).
# All movements for a Gem pair occur above the playfield before being dropped.
# There is only one descending Gem pair in play at any given time.
# In the image above (left), the red-yellow Gem pair (inside the dashed-rectangle) would appear after the green-blue Gem pair (inside the solid rectangle) has already settled.
# Power Gem Formation Priority
# gems4
#
# gems4a
#
# When a cluster of same-colored individual gems are set to form a Power Gem, but there is more than one possible configuration, priority goes to the potential Power Gem that is higher in elevation.
# In the first image above, after the green gems shatter, one of two possible Power Gems (that share resources) can be formed: a 2 x 2 block as shown in the image to the right, or a 2 x 2 block resting on the playfield floor. The Power Gem in the image to the right is the end result because it is higher in elevation.
# In the second image above, the individual red gems fall after the green gems (left image) have been cleared (middle image). The resulting Power Gem is shown on the right side, where the 2 x 3 forms due to its higher elevation.
#
# gems4b
#
# If two possible Power Gems with the same elevation can be formed, priority goes to the Power Gem that expands horizontally
# Above, a Rainbow Gem will land on the green gem (left), thereby destroying all green gems and allowing the individual red gems to fall (middle). Two possible Power Gems can form as a result, both having the same elevation. In this case, the result is the Power Gem on the right (as opposed to a 2 x 3 "vertical" Power Gem that occupies the 4th and 5th columns).
#
# gems3
#
# When a cluster of unmerged same-colored Gems drops and results in a merge, the individual Gems will combine before combining with Power Gems.
# In the image above (left), the green Crash Gem is about to eliminate the group of green Gems, allowing the 3 red Gems and 1 blue Gem to drop. The 3 red Gems will join the other 3 red Gems below, and form a 2 x 3 Power Gem before merging with the other 2 x 3 red Power Gem to its right, to finally become a 4 x 3 Power Gem. The result is the image to the right.
#
# gems2
#
# In the case where an existing Power Gem can expand by increasing vertically or horizontally, priority goes to horizontal growth.
# In the image above (left), a green Crash Gem is about to eliminate a cluster of green Gems, allowing the Gems above to drop and land on the remaining Gems below.
# Since priority goes to horizontal growth, the 2 x 2 red Power Gem will become a 3 x 2 Power Gem instead of a 2 x 3 Power Gem. The result is shown on the right.
#
# How Moves Work:
# At the start of a move, a Gem pair appears above the playfield.
# The pair falls, and each Gem in the pair land on another Gem or the playfield floor.
# All effects (eg. Power Gem formation, gem shattering due to Crash Gems or Rainbow Gems) initiated by any Gems will occur simultaneously.
# If any Gems are cleared (by Crash Gems or Rainbow Gems) in the process leaving some Gems suspended in air, all suspended Gems fall and land together.
# While step 4 makes an effect, repeat steps 3 and 4
# Below, the green Gem will combine with other adjacent ones to form a Power Gem, and at the same time the blue Crash Gem will shatter along with the two blue Gems below. The result is the middle frame, rather than the last frame.
#
# gems5
#
# Input
# Your function will receive a 2-D array/list. Each subarray has a length of 2 and consists of:
#
# a 2-character string representing a Gem pair
# a string of instructions for the Gem pair
# Each Gem is represented by the first letter of its color in uppercase — R, B, G, or Y.
# Crash Gems are represented by the first letter of its color in lowercase.
# A Rainbow Gem is represented as 0.
#
# Movement Instructions are as follows:
#
# L: move left
# R: move right
# A: rotate counter-clockwise
# B: rotate clockwise
# Output
# Your function will return the ending game state in the form of a string. The string should consist of all 12 rows joined by newline characters.
# If at any point in the game a stack of Gems goes above the top row, terminate the process and return the game state before the last move. This applies to Crash Gems and Rainbow Gems as well; their position is taken into account before their effect.
#
# Test Example
# instructions = [
#     ['BR','LLL'],
#     ['BY','LL'],
#     ['BG','ALL'],
#     ['BY','BRR'],
#     ['RR','AR'],
#     ['GY','A'],
#     ['BB','AALLL'],
#     ['GR','A'],
#     ['RY','LL'],
#     ['GG','L'],
#     ['GY','BB'],
#     ['bR','ALLL'],
#     ['gy','AAL']
# ]
# game_state = '\n'.join([
#     '      ',
#     '      ',
#     '      ',
#     '      ',
#     '      ',
#     '      ',
#     '      ',
#     '      ',
#     '      ',
#     '    R ',
#     ' R  YR',
#     'RR  RB'
# ])
#
# puzzle_fighter(instructions) == game_state #True
#
# ''' STEP-BY-STEP MOVES SEQUENCE
#    (GAME STATE at end of each of the first 5 moves)
#
#  MOVE 1      MOVE 2      MOVE 3      MOVE 4      MOVE 5
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║      ║    ║      ║    ║      ║
# ║      ║    ║      ║    ║ B    ║    ║ B    ║    ║ B    ║
# ║B     ║    ║BB    ║    ║BB    ║    ║BB    ║    ║BB  RR║
# ║R     ║    ║RY    ║    ║RYG   ║    ║RYG YB║    ║RYG YB║
# '''
# Technical Details
# Input will always be valid.
# Full Test Suite: 10 fixed tests and 200 random tests
# The maximum number of moves in any given test is 100
# Use Python 3+ for the Python translation
# For JavaScript, most built-in prototypes are frozen, except Array and Function
# Special thanks goes out to @Blind4Basics for his contributions to this kata
#
# If you enjoyed this kata, be sure to check out my other katas.
#
# GamesLogicGame SolversAlgorithms
# Solution
from collections import defaultdict

ROTATIONS   = [[1,0], [0,-1], [-1,0], [0,1]]
DIRS_POWA   = [[0,-1], [0,1], [1,0], [-1,0]]
DIRS_SINGLE = [[0,1], [1,0]]

C,X,Y,H,W,S = range(6)

LX,LY = 12,6

START = (0,3,0)

RL = "RL"
AB = "AB"
L  = "L"
A  = "A"

CRASH_GEMS = "rgby"


def puzzle_fighter(arrMoves):

    board = [[None]*LY for _ in range(LX)]
    gemsByColors = defaultdict(set)

    def getStartPoses(moves, c1, c2):
        x,y,iR = START

        for m in moves:

            if m in RL:
                y += -1 if m==L else 1

            if m in AB:
                iR += -1 if m==A else 1

            iR %= 4

            dy = ROTATIONS[iR][1]

            if y>=LY or y+dy>=LY:
                y = min(LY-1, LY-1-dy)

            elif y<0 or y+dy<0:
                y = max(0, -dy)

        dx,dy = ROTATIONS[iR]

        if dx < 0:
            x += 1

        return [[x,y,c1],[x+dx,y+dy,c2]]

    def moveGem(x0,y,x):

        g = board[x0][y]

        c,_,_,h,w,s = g

        g[X],g[Y] = x,y

        gemsByColors[c].remove((x0,y))
        gemsByColors[c].add((x,y))

        for dx in reversed(range(h)):
            for yy in range(y,y+w):

                board[x0+dx][yy] = None
                board[x+dx][yy] = g

    def couldFallFromAbove(x,y,w):

        out = set()

        x -= 1

        if x < 0:
            return out

        for yy in range(y,y+w):

            g = board[x][yy]

            if g:
                out.add((g[X],g[Y]))

        return out

    def drop(posToDrop):

        movedGems = set()

        toDrop = sorted(posToDrop)

        while toDrop:

            x,y = toDrop.pop()

            if board[x][y] is None:
                continue

            c,x0,y0,h,w,_ = board[x][y]

            while x+h < LX and all(board[x+h][yy] is None for yy in range(y,y+w)):
                x += 1

            if x == x0 and x > 1:
                continue

            movedGems.add((x,y))

            moveGem(x0,y,x)

            for nx,ny in couldFallFromAbove(x0,y,w):

                i=0
                while i<len(toDrop) and toDrop[i][0]<nx:
                    i+=1

                toDrop.insert(i,(nx,ny))

        return movedGems

    def flood(color,x,y):

        what = color + color.swapcase()

        bag = {(x,y)}
        seen = {(x,y)}

        while bag:

            new=set()

            for a,b in bag:

                for da,db in ROTATIONS:

                    na,nb = a+da, b+db

                    if not (0<=na<LX and 0<=nb<LY):
                        continue

                    g = board[na][nb]

                    if g and g[C] in what and (na,nb) not in seen:
                        new.add((na,nb))

            seen |= new
            bag = new

        roots=set()

        for a,b in seen:
            roots.add((board[a][b][X], board[a][b][Y]))

        return roots if len(roots)>1 else set()

    def explode(movedGems):

        colorsToExplode = ["0"]

        for x,y in gemsByColors["0"]:
            if x < LX-1:
                colorsToExplode.append(board[x+1][y][C])
                colorsToExplode.append(board[x+1][y][C].swapcase())

        colorsToExplode=set(colorsToExplode)

        posToExplode=set()

        for c in colorsToExplode:
            posToExplode |= gemsByColors[c]

        for c in CRASH_GEMS:

            for x,y in gemsByColors[c]:
                posToExplode |= flood(c,x,y)

        toDropNext=set()

        for x,y in posToExplode:

            c,x,y,h,w,_ = board[x][y]

            for pos in couldFallFromAbove(x,y,w):
                toDropNext.add(pos)

            gemsByColors[c].discard((x,y))

            for xx in range(x,x+h):
                for yy in range(y,y+w):
                    board[xx][yy]=None

        movedGems -= posToExplode
        toDropNext -= posToExplode

        return movedGems,toDropNext

    def makePowa(movedGems,toDropNext):

        gemAreasByCols=defaultdict(set)

        for x,y in movedGems:

            c,_,_,h,w,_=board[x][y]

            gemAreasByCols[c]|=flood(c,x,y)

        q=list(gemAreasByCols.items())

        while q:

            c,areas=q.pop()

            fresh,removed=iGotThePowa(areas,toDropNext)

            gemsByColors[c]-=removed

            if fresh:
                q.insert(0,(c,fresh))

        return toDropNext

    def iGotThePowa(areas,toDropNext):

        ones=[]
        powa=[]

        for x,y in areas:

            g=board[x][y]

            if g[S]==1:
                ones.append(g)
            else:
                powa.append(g)

        fresh=set()
        removed=set()

        for grp,isSingle in [(ones,True),(powa,False)]:

            grp.sort()

            for g in grp:

                c,x,y,h,w,s=g

                if id(g)!=id(board[x][y]) or x==LX-1 or y==LY-1:
                    continue

                expanded=expand(DIRS_SINGLE if isSingle else DIRS_POWA,isSingle,c,x,y,h,w,s)

                if expanded:

                    x,y,h,w,s = g[1:] = expanded

                    if isSingle:
                        powa.append(g)

                    fresh.add((x,y))

                    toRemove=set()

                    for xx in range(x,x+h):
                        for yy in range(y,y+w):
                            board[xx][yy]=g
                            toRemove.add((xx,yy))

                    toRemove.remove((x,y))

                    removed |= toRemove

                    cross = toDropNext & toRemove

                    if cross:
                        toDropNext.add((x,y))
                        toDropNext -= cross

        return fresh,removed

    def expand(dirs,isSingle,c,x,y,h,w,s):

        data=start=[x,y,h,w]

        if isSingle:

            triad=[board[x+dx][y+dy] for dx,dy in [(0,1),(1,0),(1,1)]]

            if any(g is None for g in triad):
                return []

            if not all(g[C]==c and g[S]==1 for g in triad):
                return []

            data=[x,y,2,2]

        for dx,dy in dirs:

            x,y,h,w=data

            while True:

                rngX=range(x,x+h) if dx==0 else [x+dx+(h-1 if dx==1 else 0)]
                rngY=range(y,y+w) if dy==0 else [y+dy+(w-1 if dy==1 else 0)]

                collect=collectNextLine(rngX,rngY,dx,dy,isSingle,c,x,y,h,w,s)

                if not collect:
                    break

                if dx!=0:
                    if dx==1:
                        h+=1
                    else:
                        x-=1
                        h+=1

                if dy!=0:
                    if dy==1:
                        w+=1
                    else:
                        y-=1
                        w+=1

                if isSingle or goodAlignment(collect,dx,dy,x,y,h,w):
                    data=[x,y,h,w]

        if start!=data:

            x,y,h,w=data

            return [x,y,h,w,h*w]

        return []

    def collectNextLine(rngX,rngY,dx,dy,isSingle,c,x,y,h,w,s):

        collect=set()

        for a in rngX:
            for b in rngY:

                if not (0<=a<LX and 0<=b<LY):
                    continue

                g=board[a][b]

                if g is None:
                    return []

                if g[C]!=c:
                    return []

                if isSingle and g[S]>1:
                    return []

                if dx!=0 and not (y<=g[Y]<y+w and y<g[Y]+g[W]<=y+w):
                    return []

                if dy!=0 and not (x<=g[X]<x+h and x<g[X]+g[H]<=x+h):
                    return []

                collect.add(tuple(g))

        return collect

    def goodAlignment(collect,dx,dy,x,y,h,w):

        if dy==-1:
            return all(g[Y]==y for g in collect)

        if dy==1:
            return all(g[Y]+g[W]==y+w for g in collect)

        if dx==-1:
            return all(g[X]==x for g in collect)

        return all(g[X]+g[H]==x+h for g in collect)

    for pair,moves in arrMoves:

        gemsPair=getStartPoses(moves,pair[0],pair[1])

        if not all(board[x][y] is None for x,y,_ in gemsPair):
            break

        for x,y,c in gemsPair:

            board[x][y]=[c,x,y,1,1,1]

            gemsByColors[c].add((x,y))

        toDrop={(x,y) for x,y,_ in gemsPair}

        while toDrop:

            moved=drop(toDrop)

            powaAndDrop=explode(moved)

            toDrop=makePowa(*powaAndDrop)

    return "\n".join(
        "".join(" " if g is None else g[C] for g in row)
        for row in board
    )