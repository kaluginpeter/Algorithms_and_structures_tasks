# Terminal Game - Create Hero Prototype
# In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:
#
# attribute	value
# name	user argument or 'Hero'
# position	'00'
# health	100
# damage	5
# experience	0
# FUNDAMENTALS
# Solution
class Hero(object):
    def __init__(self, name='Hero', position='00', health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience