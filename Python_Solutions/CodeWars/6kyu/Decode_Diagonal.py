# Decode the diagonal.
# Given a grid of characters. Output a decoded message as a string.
#
# Input
#
#   H Z R R Q
#   D I F C A E A !
#   G H T E L A E
#   L M N H P R F
#   X Z R P E
# Output
#
# HITHERE! (diagonally down right ↘ and diagonally up right ↗ if you can't go further).
#
# The message ends when there is no space at the right up or down diagonal.
#
# To make things even clearer: the same example, but in a simplified view
#
#   H _ _ _ _
#   _ I _ _ _ _ _ !
#   _ _ T _ _ _ E
#   _ _ _ H _ R _
#   _ _ _ _ E
# ALGORITHMS