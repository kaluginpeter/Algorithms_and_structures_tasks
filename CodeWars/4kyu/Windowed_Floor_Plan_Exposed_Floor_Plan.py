# Overview
# Poor window placement can expose large portion of a building's interior to outside view.
#
# As part of a floor plan evaluation system, you need to measure how much of the interior is exposed through windows.
#
# Input
# A string floor_plan, which consists of only 3 characters:
#
# ' ' (whitespace) representing empty space
# '#' representing walls
# '=' representing windows
# All lines in the input will have equal length.
#
# Terminology
# Room
#
# A room is defined as an enclosed area of empty space surrounded by walls and/or windows. If the enclosure has an opening, then it is not considered a room.
# Connectivity between spaces is orthogonal only (left, right, up, down), no diagonal adjacency.
# Example :
#  ########        ####=##        #### ##         #######       #########
#  #      #        #     #        #     #        #       #      #        ######
#  #      #        =     #        #     #        #       #      ####  ###      #
#  #      #        #     #        #     #        #       #        #             #
#  ########        ####=##        ###=###         #######          #################
#
#  (A room)        (A room)     (Not a room)      (A room)         (A room)
# Outside
#
# Any empty space connected to the edge of the floor plan is considered outside.
# Areas beyond the boundaries of the floor plan are also considered outside.
# Windows
#
# A special cell that allows exposure lines to pass through it.
# Windows are not considered spaces themselves.
# Exposure Mechanic
# Exposure originates from outside-facing windows.
# A window emits exposure only if at least one of its orthogonally adjacent cells are outside. Exposure then propagates from the window in the opposite direction(s).
# Exposure propagates orthogonally in a straight line through rooms and windows. Walls and outside spaces block exposure.
# Room spaces reached by exposure are considered exposed.
# Exposure lines do not block one another and may overlap.
# Examples :
#
#     X = exposed space
#
#     ##########         ##########
#     #    #   #         #    #   #
#     =    #   #   =>    =XXXX#   #
#     #    #   #         #    #   #
#     ##########         ##########
#
#     ##########       ##########
#     #    #   #       #    #   #
#     #    #   #       #    #   #
#     =    =   #   =>  =XXXX=XXX#
#     #    #   #       #    #   #
#     ##########       ##########
#
#     ###=##            ###=##
#     #    #            #  X #
#     =    #    =>      =XXXX#
#     #    #            #  X #
#     ###=##            ###=##
# Output
# Return a float representing the percentage of the room area that is exposed.
#
# Only room spaces contribute to the total room area and exposed area.
#
# For the sake of this kata, 0/0 results in 0.
#
# Note : The inputs are not guaranteed to represent realistic architecture. Even unusual or unrealistic floor plans should still be interpreted strictly according to the rules above.
#
# Constraints
# Grid dimensions range from 1x1 to 500x500
#
# Examples
# For visualization : X = exposed space, . = unexposed space
#
# 1.   ####==##           ####==##
#      #      #           #...XX.#
#      #      #           #...XX.#
#      ####=###    =>     ####=###
#      #      #           #...X..#
#      #      =           #XXXXXX=
#      ########           ########
#
#      Output : 45.8333333 (11 out of 24)
#
# 2.   ########           ########
#      #   #  #           #...#..#
#      =   #  #    =>     =XXX#..#
#      #   =  #           #...=..#
#      ########           ########
#
#      Output : 20.0 (3 out of 15)
#
# 3.   ######             ######
#      #     =            #XXXXX=
#      #      #    =>     #.....X#
#      #      #           #.....X#
#      ########           ########
#
#      Output : 41.1764705 (7 out of 17)
#
# 4.   ####=###           ####=###
#      #      #           #...X..#
#      ###    #           ###.X..#
#      #   ####    =>     #...####
#      #      #           #......#
#      #      #           #......#
#      ########           ########
#
#      Output : 8.0 (2 out of 25)
#
# 5.   ##=#####
#      #      =
#      #      ######
#      #
#      ####=########
#
#      Output : 0.0 (0 out of 0)
#
#      No rooms here.
# Floor Plan Mini-Series
# Good Floor Plan, Discombobulated Floor Plan
# Windowed Floor Plan, Exposed Floor Plan
# GraphsAlgorithms
# Solution
from collections import deque

def exposure_percentage(floor_plan: str) -> float:
    g = floor_plan.split('\n')
    H = len(g)
    W = len(g[0])
    outside = [[False] * W for _ in range(H)]
    vis = [[False] * W for _ in range(H)]
    q = deque()
    for r in range(H):
        for c in (0, W - 1):
            if g[r][c] == ' ' and not vis[r][c]:
                vis[r][c] = True
                outside[r][c] = True
                q.append((r, c))

    for c in range(W):
        for r in (0, H - 1):
            if g[r][c] == ' ' and not vis[r][c]:
                vis[r][c] = True
                outside[r][c] = True
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < H and 0 <= nc < W:
                if not vis[nr][nc] and g[nr][nc] == ' ':
                    vis[nr][nc] = True
                    outside[nr][nc] = True
                    q.append((nr, nc))
    room = [[False]*W for _ in range(H)]
    vis = [[False]*W for _ in range(H)]
    total = 0
    for r in range(H):
        for c in range(W):
            if g[r][c] != ' ' or vis[r][c]: continue
            comp = []
            q = deque([(r,c)])
            vis[r][c] = True
            ok = True
            while q:
                x,y = q.popleft()
                comp.append((x,y))
                if outside[x][y]: ok = False
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<H and 0<=ny<W:
                        if g[nx][ny]==' ' and not vis[nx][ny]:
                            vis[nx][ny]=True
                            q.append((nx,ny))
            if ok:
                total += len(comp)
                for x,y in comp: room[x][y]=True
    if total == 0: return 0.0
    exposed = [[False]*W for _ in range(H)]
    visited = [[[False]*4 for _ in range(W)] for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(H):
        for c in range(W):
            if g[r][c] != '=': continue
            for k,(dr,dc) in enumerate(dirs):
                orow = r+dr
                ocol = c+dc
                if not (0<=orow<H and 0<=ocol<W): is_outside = True
                else: is_outside = outside[orow][ocol]
                if not is_outside: continue
                rr = r-dr
                cc = c-dc
                while 0<=rr<H and 0<=cc<W:
                    if visited[rr][cc][k]: break
                    visited[rr][cc][k]=True
                    if g[rr][cc]=='#': break
                    if outside[rr][cc]: break
                    if room[rr][cc]: exposed[rr][cc]=True
                    rr -= dr
                    cc -= dc
    cnt = 0
    for r in range(H):
        for c in range(W):
            if exposed[r][c]: cnt += 1
    return cnt * 100.0 / total