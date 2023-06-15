# Funny Dots
# You will get two integers n (width) and m (height) and your task is to draw the following pattern.
# Each line is seperated with a newline (\n)
#
# Both integers are equal or greater than 1; no need to check for invalid parameters.
#
# Examples
#
#                                             +---+---+---+
#              +---+                          | o | o | o |
# dot(1, 1) => | o |            dot(3, 2) =>  +---+---+---+
#              +---+                          | o | o | o |
#                                             +---+---+---+
#
# Serie: ASCII Fun
# ASCII Fun #1: X-Shape
# ASCII Fun #2: Funny Dots
# ASCII Fun #3: Puzzle Tiles
# ASCII Fun #4: Build a pyramid
# ASCII ART
# Solution
def dot(n, m):
    return ("+---" * n + "+\n" + "| o " * n + "|\n") * m + ("+---" * n + "+")