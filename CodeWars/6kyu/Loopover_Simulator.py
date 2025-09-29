# Loopover
# Loopover is a single-player sliding tile puzzle game originally created by carykh. There is a 1 kyu kata that is about solving the puzzle. This particular kata is probably the first step to trying to approach that hard problem - simulating the puzzle. All of the rules are explained in that kata, except this one will only use numbers.
#
# Basic instructions
# How do moves work?
#
# U{n} -> You shift the nth column up by one unit. The number at the very top will be moved to the bottom position.
# D{n} -> You shift the nth column down by one unit. The number at the very bottom will be moved to the top position.
# R{n} -> You shift the nth row right by one unit. The number at the right will be moved to the left position.
# L{n} -> You shift the nth row left by one unit. The number at the left will be moved to the right position.
# How does Loopover class work?
#
# The class is initialised with a single parameter - grid_size, which is the size of the grid.
# move -> Takes the string representation of a single move, and applies it via mutating internal state. Should not return anything.
# output -> Takes no arguments and returns the current state of the puzzle as a two dimensional array of integers.
# A few notes
#
# You don't need to check the moves for validity.
# The internal state must stay the same after mutating the outcome of output.
# Task
# Given a class Loopover with the initial board size (0 < grid_size < 100), output method and move method. Define the methods move and output such that they simulate the puzzle on a given size grid.
#
# Example
# puzzle = Loopover(5)
# puzzle.output()
# # [[ 1, 2,  3,  4,  5 ],
# #  [ 6, 7,  8,  9,  10],
# #  [11, 12, 13, 14, 15],
# #  [16, 17, 18, 19, 20],
# #  [21, 22, 23, 24, 25]]
#
# puzzle.move("U2")
# puzzle.output()
# # [[ 1,  7,  3,  4,  5],
# #  [ 6, 12,  8,  9, 10],
# #  [11, 17, 13, 14, 15],
# #  [16, 22, 18, 19, 20],
# #  [21,  2, 23, 24, 25]]
#
# puzzle.move("R3")
# puzzle.output()
# # [[ 1,  7,  3,  4,  5],
# #  [ 6, 12,  8,  9, 10],
# #  [15, 11, 17, 13, 14],
# #  [16, 22, 18, 19, 20],
# #  [21,  2, 23, 24, 25]]
#
# puzzle.move("L4")
# puzzle.output()
# # [[ 1,  7,  3,  4,  5],
# #  [ 6, 12,  8,  9, 10],
# #  [15, 11, 17, 13, 14],
# #  [22, 18, 19, 20, 16],
# #  [21,  2, 23, 24, 25]]
#
# puzzle.move("D5")
# puzzle.output()
# # [[ 1,  7,  3,  4, 25],
# #  [ 6, 12,  8,  9,  5],
# #  [15, 11, 17, 13, 10],
# #  [22, 18, 19, 20, 14],
# #  [21,  2, 23, 24, 16]]
# GamesAlgorithms
# Solution
from copy import deepcopy


class Loopover:
    def __init__(self, grid_size: int) -> None:
        self.grid_size = grid_size
        self.grid: list[list[int]] = []
        ptr: int = 1
        for i in range(grid_size):
            row: list[int] = list(range(ptr, ptr + grid_size))
            self.grid.append(row)
            ptr += grid_size

    def output(self) -> list[list[int]]:
        return deepcopy(self.grid)

    def move(self, s: str) -> None:
        ptr: int = int(s[1:]) - 1
        match ord(s[0]) - 65:
            case 20:  # U
                dataset: list[int] = [self.grid[i][ptr] for i in range(self.grid_size)]
                dataset = dataset[1:] + dataset[:1]
                for i in range(self.grid_size): self.grid[i][ptr] = dataset[i]
                return
            case 3:  # D
                dataset: list[int] = [self.grid[i][ptr] for i in range(self.grid_size)]
                dataset = dataset[-1:] + dataset[:-1]
                for i in range(self.grid_size): self.grid[i][ptr] = dataset[i]
                return
            case 11:  # L
                self.grid[ptr] = self.grid[ptr][1:] + self.grid[ptr][:1]
                return
            case _:  # R
                self.grid[ptr] = self.grid[ptr][-1:] + self.grid[ptr][:-1]