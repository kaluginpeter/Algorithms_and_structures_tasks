# The Adapter Design Pattern can be used, for example in the StarCraft game, to insert an external character in the game.
#
# The pattern consists in having a wrapper class that will adapt the code from the external source.
#
# Your Task
# The adapter receives an instance of the object that it is going to adapt and handles it in a way that works with our application.
#
# In this example we have the pre-loaded classes:
#
# class Target:
#     def __init__(self, health):
#         self.health = health
#
# class Marine:
#     @staticmethod
#     def attack(target):
#         target.health -= 6
#
# class Zealot:
#     @staticmethod
#     def attack(target):
#         target.health -= 8
#
# class Zergling:
#     @staticmethod
#     def attack(target):
#         target.health -= 5
#
# class Mario:
#     @staticmethod
#     def jump_attack():
#         print('Mamamia!')
#         return 3
# Complete the code so that we can create a MarioAdapter that can attack as other units do.
#
# Note to calculate how much damage mario is going to do you have to call the jumpAttack method (jump_attack in Python).
#
# Resources
# PatternCraft > Adapter
# SourceMaking > Adapter
# Wikipedia > Adapter
# PatternCraft series
# State Pattern
# Strategy Pattern
# Visitor Pattern
# Decorator Pattern
# Adapter Pattern
# Command Pattern
# The original PatternCraft series (by John Lindquist) is a collection of Youtube videos that explains some of the design patterns and how they are used (or could be) on StarCraft.
#
# DESIGN PATTERNSFUNDAMENTALS
# Solution
class MarioAdapter:
    def __init__(self, mario=None):
        if mario is None:
            raise TypeError("MarioAdapter.__init__() missing 1 required positional argument: 'mario'")
        self.mario = mario

    def attack(self, target):
        target.health -= self.mario.jump_attack()