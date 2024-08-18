# The knight is a piece in the game of chess. It may move two squares vertically and one square horizontally or two squares horizontally and one square vertically. For a visual representation of the possible moves, take a look here (second image).
#
# Given the current position of the knight on the chessboard (e.g."b8") return all its possible next positions, alphabetically sorted (e.g. ["a6", "c6", "d7"])
#
# Your code can be maximum 170 150 bytes long (I underestimated your skills ;-)
#
#
# Note: this is the code golf version of this kata
#
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
#
# Translations are welcome!
# ...except for Ruby, which will arrive soon
#
# RESTRICTEDPUZZLES
# Solution
def next_pos(p):d=int(p[1]);i=ord(p[0])-97;h=[-2,-1,1,2];return [chr(i+x+97)+str(d+y)for x in h for y in h if abs(x)!=abs(y)and(0<=i+x<8)&(1<=d+y<=8)]