# You are a zoologist studying the little-known Python species Applicatus Serpens Characteribus Instructus Informaticus or in short ASCII-Python.
#
# All known specimens share a distinctive anatomy: a head with two eyes and a tongue, followed by a segmented torso.
#
# Below is a photograph of two young specimens measuring 13 cm and 21 cm, respectively:
#
# (o>o)-0-0-0-0
#
# (o>o)-0-0-0-0-0-0-0-0
# During your research, you become particularly interested in modeling the eyes of the ASCII-Python. To your surprise, you discover a remarkable property: from the eye configuration alone, it is possible to perfectly deduce the total body length of the snake.
#
# This unexpected finding ensures that your research funding will, thankfully, continue for another year (phew).
#
# To formalize your model, you use the official snake research language: Python.
#
# Your model is initialized as:
#
# o = SnakeEye()
# Once initialized, applying the built-in len() function to a photograph of an individual ASCII-Python yields its length in centimeters. For example:
#
# len((o>o)-0-0-0-0)
# returns:
#
# 13
# To test your model, you want to make sure it works on previously documented specimens from the example test cases before performing a full study in the wild for submission.
#
# Good Luck!
#
# Note:
# This task is meant to explore and experiment with language features rather than strictly follow coding conventions. If you get stuck, this resource might help.
#
# Puzzles
# Solution
class Snake:
    def __init__(self):
        self.segments = 0

    def __sub__(self, other):
        if other == 0:
            self.segments += 1
            return self

    def __len__(self):
        return 5 + self.segments * 2

class SnakeEye:
    def __gt__(self, other):
        return Snake()