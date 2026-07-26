# Touch typing is a typing technique where each hand is responsible for specific keys on the keyboard.
#
# In this kata, you will simulate this behaviour using a simplified keyboard layout based on a QWERTY keyboard.
#
# Keyboard layout
# Left hand letters
# qwert
# asdfg
# zxcvb
# Right hand letters
# yuiop
# hjkl
# nm
# Task
# Write a function that receives a single lowercase word ( without any spaces ), and returns:
#
# NONE if the word is empty
# LEFT if the word can be typed using only the left hand
# RIGHT if the word can be typed using only the right hand
# BOTH if the word requires both hands
# The word will be encoded as a reusable iterable, yielding strings of single letters.
#
# Rules
# Input contains only lowercase letters a to z
# Use only the keyboard layout provided above
# The word can be infinite ( this will only be tested with words with a finite prefix typed on both sides of the keyboard )
# Preloaded
# class Hand(enum.IntEnum):
#     NONE  = 0;
#     LEFT  = 1;
#     RIGHT = 2;
#     BOTH  = 3;
# Examples
# ""       ->  NONE
# "gaffe"  ->  LEFT
# "cards"  ->  LEFT
# "milk"   ->  RIGHT
# "pill"   ->  RIGHT
# "type"   ->  BOTH
# Credit
# This kata was inspired by One or Two Hands? ( retired ) by Gonzalo Vidal.
# Solution
from collections.abc import Iterable;
from preloaded import Hand;
(NONE,LEFT,RIGHT,BOTH) = Hand;

def which_hand(word: Iterable[str]) -> Hand:
    left: str = 'qwertasdfgzxcvb'
    right: str = 'yuiophjklnm'
    was: bool = False
    is_left: bool = False
    is_right: bool = False
    for ch in word:
        was = True
        if ch in left: is_left = True
        elif ch in right: is_right = True
        if is_left and is_right: break
    if not was: return NONE
    return BOTH if (is_left and is_right) else [RIGHT, LEFT][is_left]