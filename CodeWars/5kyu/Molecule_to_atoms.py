# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).
#
# For example:
#
# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}
#
# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}
#
# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.
#
# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
#
# PARSINGALGORITHMSSTRINGS
# Solution
from collections import defaultdict


class Solution:
    current_atom: str = ''
    current_points: int = 0

    def add_atom(self, current_group: dict[str, int]) -> None:
        current_group[self.current_atom] += self.current_points if self.current_points else 1
        self.current_atom = ''
        self.current_points = 0

    def extend_groups(self, current_group: dict[str, int], prev_group: dict[str, int]) -> None:
        for atom in prev_group:
            current_group[atom] += prev_group[atom]

    def countOfAtoms(self, formula: str) -> str:
        print(formula)
        atoms: dict[str, int] = defaultdict(int)
        stack: list[dict[str, int]] = []

        idx: int = 0
        while idx < len(formula):
            if formula[idx].islower():
                self.current_atom += formula[idx]
                idx += 1

            elif formula[idx].isupper():
                if self.current_atom: self.add_atom(atoms)
                self.current_atom = formula[idx]
                idx += 1

            elif formula[idx] in '{[(':
                if self.current_atom: self.add_atom(atoms)

                stack.append(atoms)
                atoms = defaultdict(int)
                idx += 1

            elif formula[idx] in '}])':
                if self.current_atom: self.add_atom(atoms)

                idx += 1
                while idx < len(formula) and formula[idx].isdigit():
                    self.current_points = self.current_points * 10 + int(formula[idx])
                    idx += 1
                self.current_points = max(self.current_points, 1)

                for atom in atoms:
                    atoms[atom] = self.current_points * atoms[atom]
                self.current_points = 0

                if stack: self.extend_groups(atoms, stack.pop())

            elif formula[idx].isdigit():
                self.current_points = self.current_points * 10 + int(formula[idx])
                idx += 1

        if self.current_atom: self.add_atom(atoms)

        while stack:
            self.extend_groups(atoms, stack.pop())

        return atoms


def parse_molecule(formula):
    return Solution().countOfAtoms(formula)