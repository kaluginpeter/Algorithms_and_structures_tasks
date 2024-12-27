# Leaderboard climbers
# In this kata you will be given a leaderboard of unique names for example:
#
# ['John',
#  'Brian',
#  'Jim',
#  'Dave',
#  'Fred']
# Then you will be given a list of strings for example:
#
# ['Dave +1', 'Fred +4', 'Brian -1']
# Then you sort the leaderboard.
#
# The steps for our example would be:
#
# # Dave up 1
# ['John',
#  'Brian',
#  'Dave',
#  'Jim',
#  'Fred']
# # Fred up 4
# ['Fred',
#  'John',
#  'Brian',
#  'Dave',
#  'Jim']
# # Brian down 1
# ['Fred',
#  'John',
#  'Dave',
#  'Brian',
#  'Jim']
# Then once you have done this you need to return the leaderboard.
#
# All inputs will be valid. All strings in the second list will never ask to move a name up higher or lower than possible eg. "John +3" could not be added to the end of the second input list in the example above.
#
# The strings in the second list will always be something in the leaderboard followed by a space and a + or - sign followed by a number.
#
# ListsFundamentals