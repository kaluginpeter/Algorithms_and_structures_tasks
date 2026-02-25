# This kata is inspired by davazp's one
# Context
# So, here we go again:
#
# You are given an ASCII diagram, containing minus signs "-", plus signs "+", vertical bars "|" and whitespaces " " . Your task is to write a function which will break the diagram in the minimal pieces it is made of.
#
# For example, if the input of your function is the diagram on the left below, the expected answer will be the list of strings representing the three individual shapes on the right (note how the biggest shape lost a "+" sign in the extraction) :
#
# Input:                          Expected:
# +------------+                  +------------+
# |            |                  |            |    +------+    +-----+
# |            |                  |            |    |      |    |     |
# |            |                  |            |    |      |    |     |
# +------+-----+                  +------------+    +------+    +-----+
# |      |     |
# |      |     |
# +------+-----+
# If you encounter imbricated pieces, both outer and inner shapes have to be returned. For example:
#
# Input:                          Expected:
# +------------+                  +------------+
# |            |                  |            |
# |    +--+    |                  |    +--+    |
# |    |  |    |                  |    |  |    |
# |    |  |    |                  |    |  |    |    +--+
# |    +--+    |                  |    +--+    |    |  |
# |            |                  |            |    |  |
# +------------+                  +------------+    +--+
# So... What's new!?
# What is new in this "evilized" version is that you'll have to manage the extraction of shapes without inner whitespaces.
#
# For example, the input below should lead to the following list of strings:
#
# Input:                          Expected:
# +------------+                  +------------+
# |            |                  |            |    +------+    +----+    ++
# |            |                  |            |    |      |    |    |    ||
# |            |                  |            |    |      |    |    |    ||
# +------++----+                  +------------+    +------+    +----+    ++
# |      ||    |
# |      ||    |
# +------++----+
# From there, you'll have two approaches...:
#
# The "easy" (better) one...
# ... or the hard one: if you stumble frequently going through the fixed tests, might be you didn't made the right move and you're on this path. It's doable that way either, but it is way harder than the other one (1 or 2 kyu ranks higher! But if you like challenges, you can try that really evilized way... ;) )
# TASK
# You have to find all the individual pieces contained in the original diagram. Note that you are only searching for the smallest possible ones.
#
# You may find below some important indications about what you will have to deal with:
#
# The pieces should not have any spaces on their right (ie. no trailing spaces).
#
# However, they could have leading spaces if the figure is not a rectangle, as shown below:
#
#     +---+
#     |   |
# +---+   |
# |       |
# +-------+
# It is not allowed to use more leading spaces than necessary. It is to say, the first character of at least one of the lines has to be different from a space.
#
# Only explicitly closed pieces have to be considered (meaning, in the diagram above, there is one and only one piece).
#
# The borders of each shape have to contain only the meaningful plus signs "+" (those in corners or at the intersections of several straight lines).
#
# Keep an eye on the performances. You won't have to make your code unreadable to pass the tests, but be clever with what you choose to implement.
#
# After all of that, you still will have to pass the random tests...
#
# Note: In the display, to make it easier to see where whitespaces are or not, the spaces characters will be replaced with dots:
#
#  ```
#     +---+              ....+---+                  +---+                  +---+
#     |   |              ....|...|                  |   |                  |...|..      <- there are spaces here, on the right
# +---+   |      =>      +---+...|                  |   +---+      =>      |...+---+
# |       |              |.......|                  |       |              |.......|
# +-------+              +-------+                  +-------+              +-------+
# ```
#
# Input
# The diagrams are given as ordinary multiline strings of various lengths.
# Output
# A list of multilines strings (see the example tests).
# The order of the individual shapes in the list does not matter.
#
# Final notes...
# If you're following the "hard path", this kata might make you crazy...
# Tests design: about 80 fixed tests (each of them doubled) and the random ones with shapes up to around 80x80 characters (100 for python and ruby, 200 for Rust and 250 for Java). If your solution times out, do not hesitate to do a second try before to do any modification to your code.
# GamesAlgorithmsPuzzles