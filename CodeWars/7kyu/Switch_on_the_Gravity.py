# Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.
#
# Examples
# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "#", "#", "-"]
# ]
#
# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "-", "-", "-"],
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "#", "#", "-"]
# ]
#
# switch_gravity([
#   ["-", "#", "#", "#", "#", "-"],
#   ["#", "-", "-", "#", "#", "-"],
#   ["-", "#", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "#", "-", "#", "#", "-"],
#   ["#", "#", "#", "#", "#", "-"]
# ]
# Notes
# Each block falls individually, meaning there are no rigid objects. Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.
#
# ALGORITHMSMATRIXARRAYS