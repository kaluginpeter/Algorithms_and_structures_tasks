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