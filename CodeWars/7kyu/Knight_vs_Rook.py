# Knight vs Rook
# If you are not familiar with chess game you can learn more here.
#
# You will be provided with a knight's and a rook's positions on the board. Implement a function that tells us which piece can capture the other:
#
# "Rook" if the rook captures the knight
# "Knight" if the knight captures the rook
# "None" otherwise
# Check the test cases and Happy coding :)
#
# Fundamentals
# Solution
def knight_vs_rook(knight, rook):
    kr, kc = knight
    rr, rc = rook

    kc = ord(kc) - ord('A')
    rc = ord(rc) - ord('A')

    dx = abs(kr - rr)
    dy = abs(kc - rc)

    if (dx, dy) in ((1, 2), (2, 1)): return "Knight"

    if kr == rr or kc == rc: return "Rook"

    return "None"