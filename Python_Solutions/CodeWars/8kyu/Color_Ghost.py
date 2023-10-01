# Color Ghost
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
#
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"
# OBJECT-ORIENTED PROGRAMMINGFUNDAMENTALS
# Solution
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])