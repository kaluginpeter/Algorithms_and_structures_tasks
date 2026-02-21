# A sliding puzzle is a combination puzzle that challenges a player to slide (frequently flat) pieces along certain routes (usually on a board) to establish a certain end-configuration.
#
# Your goal for this kata is to write a function that produces a sequence of tile movements that solves the puzzle.
#
# Input
# An n x n array/list comprised of integer values ranging from 0 to n^2 - 1 (inclusive), which represents a square grid of tiles. Note that there will always be one empty tile (represented by 0) to allow for movement of adjacent tiles.
#
# Output
# An array/list comprised of any (but not necessarily all) of the integers from 1 to n^2 - 1, inclusive. This represents the sequence of tile moves for a successful transition from the initial unsolved state to the solved state. If the puzzle is unsolvable, return null(JavaScript, Java, PHP) or None(Python) or the vector {0} (C++).
#
# Test Example
# let simpleExample = [
#     [ 1, 2, 3, 4],
#     [ 5, 0, 6, 8],
#     [ 9,10, 7,11],
#     [13,14,15,12]
# ];
# slidePuzzle(simpleExample); // [6,7,11,12]
#
# // TRANSITION SEQUENCE:
# [ 1, 2, 3, 4]    [ 1, 2, 3, 4]    [ 1, 2, 3, 4]    [ 1, 2, 3, 4]    [ 1, 2, 3, 4]
# [ 5, 0, 6, 8]    [ 5, 6, 0, 8]    [ 5, 6, 7, 8]    [ 5, 6, 7, 8]    [ 5, 6, 7, 8]
# [ 9,10, 7,11] -> [ 9,10, 7,11] -> [ 9,10, 0,11] -> [ 9,10,11, 0] -> [ 9,10,11,12]
# [13,14,15,12]    [13,14,15,12]    [13,14,15,12]    [13,14,15,12]    [13,14,15, 0]
#
# // NOTE: Your solution does not need to follow this exact sequence to pass
# Technical Details
# Input will always be valid.
# The range of values for n are: 10 >= n >= 3
# If you enjoyed this kata, be sure to check out my other katas.
#
# PuzzlesGenetic AlgorithmsGame SolversAlgorithms
# Solution
import numpy as np
import queue


class Node():
    def __init__(self, value):
        self.value = value
        self.is_solved = False
        self.paths = []
        self.distance = np.Infinity
        self.back = None

    def __gt__(self, other):
        return self.distance > other.distance

    def clear(self):
        self.distance = np.Infinity
        self.back = None

    def distance_to(self, other):
        return abs(self.y - other.y) + abs(self.x - other.x)

    def swap(self, other):
        self.value, other.value = other.value, self.value
        self.is_solved, other.is_solved = other.is_solved, self.is_solved

    def get_paths(self, puzzle):
        height, width = puzzle.shape
        if self.y > 0:
            self.paths.append(puzzle[self.y - 1, self.x])
        if self.y < height - 1:
            self.paths.append(puzzle[self.y + 1, self.x])
        if self.x > 0:
            self.paths.append(puzzle[self.y, self.x - 1])
        if self.x < width - 1:
            self.paths.append(puzzle[self.y, self.x + 1])

    def best_adjacent(self, puzzle, relative):
        possible_paths = []

        for path in self.paths:
            if not path.is_solved: possible_paths.append((relative.distance_to(path), path))
        solution = sorted(possible_paths, key=lambda x: x[0])[0]
        return solution[1]

    def astar(self, puzzle, objective, number, ignore=None):
        ignore = ignore or []
        queuee = queue.PriorityQueue()
        self.distance = 0
        queuee.put((0, self))
        while not queuee.empty():
            _, case = queuee.get()
            if case == objective: break
            for pos_b in case.paths:
                if pos_b.back != case:
                    if pos_b != number and not pos_b.is_solved and pos_b not in ignore:
                        if pos_b.distance > 1 + case.distance:
                            pos_b.distance = 1 + case.distance
                            pos_b.back = case
                            queuee.put((pos_b.distance_to(objective), pos_b))
        node = objective
        path = []
        while (node.back):
            path.append(node)
            node = node.back
        path.append(node)
        puzzle.clear()
        return list(reversed(path))


class Graph():
    def __init__(self, array):
        self.puzzle = np.array(array, dtype=np)
        self.solved = np.zeros_like(self.puzzle, dtype=int)
        self.height, self.width = self.puzzle.shape
        self.steps = []

        for i, row in enumerate(self.puzzle):
            for j, value in enumerate(row):
                self.puzzle[i, j] = Node(value)
                self.puzzle[i, j].y, self.puzzle[i, j].x = i, j
                self.solved[i, j] = 1 + j + self.width * i
        self.solved[-1, -1] = 0
        for row in self.puzzle: [case.get_paths(self.puzzle) for case in row]

    def clear(self):
        [case.clear() for case in np.ravel(self.puzzle)]

    def traverse(self):
        self.reduce_problem()
        self.solve()

    def solve(self):
        for i in range(24):
            solution = self.puzzle[-3:, -3:].ravel().tolist()[:-1]
            solution = [s.value for s in solution]
            if sorted(solution) == solution: return True

            objective = self.find_number(0)
            if i < 12:
                if objective.y == self.height - 1 and objective.x == self.width - 1:
                    board_piece = self.puzzle[-2, -1]
                if objective.y == self.height - 2 and objective.x == self.width - 1:
                    board_piece = self.puzzle[-2, -2]
                if objective.y == self.height - 2 and objective.x == self.width - 2:
                    board_piece = self.puzzle[-1, -2]
                if objective.y == self.height - 1 and objective.x == self.width - 2:
                    board_piece = self.puzzle[-1, -1]
            if i >= 12:
                if objective.y == self.height - 1 and objective.x == self.width - 1:
                    board_piece = self.puzzle[-1, -2]
                if objective.y == self.height - 2 and objective.x == self.width - 1:
                    board_piece = self.puzzle[-1, -1]
                if objective.y == self.height - 2 and objective.x == self.width - 2:
                    board_piece = self.puzzle[-2, -1]
                if objective.y == self.height - 1 and objective.x == self.width - 2:
                    board_piece = self.puzzle[-2, -2]
            self.steps.append(board_piece.value)
            objective.swap(board_piece)
        self.steps = None

    def reduce_problem(self):
        for i in range(self.height - 2):
            helper = (self.puzzle[i + 1, -1], self.puzzle[i + 1, -2],
                      self.puzzle[i + 2, -1], self.puzzle[i + 2, -2])
            self.look_line(self.puzzle[i, :], self.solved[i, :], helper)

            helper = (self.puzzle[-1, i + 1], self.puzzle[-2, i + 1],
                      self.puzzle[-1, i + 2], self.puzzle[-2, i + 2])
            self.look_line(self.puzzle[i + 1:, i], self.solved[i + 1:, i], helper)
        return True

    def look_line(self, line, solutions, helper):
        for case, solution in zip(line[:-2], solutions[:-2]):
            self.solve_number(case, solution)
        self.solve_number(helper[2], solutions[-1], is_solved=False)
        self.solve_number(helper[3], solutions[-2], is_solved=False)

        self.solve_number(line[-1], solutions[-2], is_solved=False)
        self.solve_number(helper[0], solutions[-1], is_solved=False)

        if line[-2] != self.find_number(0):
            self.solve_number(helper[1], line[-2].value, ignore=[helper[0], line[-1]], is_solved=False)
        self.solve_number(line[-2], solutions[-2])
        self.solve_number(line[-1], solutions[-1])
        return True

    def solve_number(self, position, number, ignore=None, is_solved=True):
        while position.value != number:
            origin = self.find_number(0)
            objective = self.find_number(number)
            adjacent = objective.best_adjacent(self.puzzle, position)
            path = origin.astar(self, adjacent, objective, ignore)
            for one, two in zip(path, path[1:]):
                self.steps.append(two.value)
                one.swap(two)
            else:
                self.steps.append(objective.value)
                path[-1].swap(objective)
        if is_solved: position.is_solved = True
        return True

    def find_number(self, num):
        for row in self.puzzle:
            for node in row:
                if node.value == num: return node
        return None


def slide_puzzle(array):
    graph_repr = Graph(array)
    graph_repr.traverse()
    return graph_repr.steps