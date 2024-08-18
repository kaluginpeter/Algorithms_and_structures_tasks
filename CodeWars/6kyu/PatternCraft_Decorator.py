# The Decorator Design Pattern can be used, for example, in the StarCraft game to manage upgrades.
#
# The pattern consists in "incrementing" your base class with extra functionality.
#
# A decorator will receive an instance of the base class and use it to create a new instance with the new things you want "added on it".
#
# Your Task
# Complete the code so that when a Marine gets a WeaponUpgrade it increases the damage by 1, and if it is a ArmorUpgrade then increase the armor by 1.
#
# You have 3 classes:
#
# Marine: has a damage and an armor properties
# MarineWeaponUpgrade and MarineArmorUpgrade: upgrades to apply on marine. Accepts a Marine in the constructor and has the same properties as the Marine
# Resouces
# PatternCraft > Decorator
# SourceMaking > Decorator
# Wikipedia > Decorator
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
class Marine:
    def __init__(self, damage, armor):
        self.damage = damage
        self.armor = armor
class Marine_weapon_upgrade:
    def __init__(self, marine):
        self.marine = marine
        self.damage = self.marine.damage + 1
        self.armor = self.marine.armor

class Marine_armor_upgrade:
    def __init__(self, marine):
        self.marine = marine
        self.armor = self.marine.armor + 1
        self.damage = self.marine.damage