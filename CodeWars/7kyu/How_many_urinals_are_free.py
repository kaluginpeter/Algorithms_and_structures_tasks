# How many urinals are free?
# In men's public toilets with urinals, there is this unwritten rule that you leave at least one urinal free between you and the next person peeing. For example if there are 3 urinals and one person is already peeing in the left one, you will choose the urinal on the right and not the one in the middle. That means that a maximum of 3 people can pee at the same time on public toilets with 5 urinals when following this rule (Only 2 if the first person pees into urinal 2 or 4).
#
# Imgur Urinals
#
# Your task:
# You need to write a function that returns the maximum of free urinals as an integer according to the unwritten rule.
#
# Input
# A String containing 1s and 0s (Example: 10001) (1 <= Length <= 20)
# A one stands for a taken urinal and a zero for a free one.
#
# Examples
# 10001 returns 1 (10101)
# 1001 returns 0 (1001)
# 00000 returns 3 (10101)
# 0000 returns 2 (1001)
# 01000 returns 1 (01010 or 01001)
#
# Note
# When there is already a mistake in the input string (for example 011), then return -1
#
# Have fun and don't pee into the wrong urinal ;)
#
# Fundamentals
# Solution
def get_free_urinals(urinals):
    if '11' in urinals: return -1
    urinals_: list[str] = list(urinals)
    free: int = 0
    for i in range(len(urinals)):
        if urinals_[i] == '0':
            if (not i or urinals_[i - 1] == '0') and (i + 1 == len(urinals) or urinals_[i + 1] == '0'):
                urinals_[i] = '1'
                free += 1
    return free