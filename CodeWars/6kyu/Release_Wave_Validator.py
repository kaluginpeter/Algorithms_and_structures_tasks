# Release Wave Validator
# Write solve that checks whether an ordered deployment plan respects all prerequisite rules.
#
# A deployment plan is split into waves. All packages inside the same wave are released at the same time. A prerequisite pair (a, b) means package a may only be released after package b.
#
# Function contract
# solve(waves: list[list[str]], prerequisites: list[tuple[str, str]]) -> bool
#
# waves is an ordered list of deployment waves. Each inner list contains the package names scheduled for that wave.
#
# prerequisites is a list of (package, required_package) pairs.
#
# Return True if the plan is valid. Otherwise return False.
#
# A plan is valid only when all of these rules hold:
#
# Every package scheduled in waves appears exactly once across all waves.
# Every package mentioned in prerequisites, on either side of a pair, appears in exactly one wave.
# If (a, b) appears in prerequisites, then b must be in a strictly earlier wave than a.
# Packages in the same wave cannot satisfy each other's prerequisites.
# Duplicate prerequisite pairs may appear and do not change the answer.
# Empty waves may appear and should be ignored.
# Constraints:
#
# The total number of package names across all waves can be as large as 50000.
# The number of prerequisite pairs can be as large as 100000.
# Examples
# solve([['auth', 'db'], ['billing'], ['reports']], [('billing', 'auth'), ('billing', 'db'), ('reports', 'billing')]) -> True
#
# billing depends on auth and db, and both are released earlier. reports depends on billing, which is also earlier.
#
# solve([['auth', 'billing'], ['db']], [('billing', 'auth')]) -> False
#
# billing and auth are released in the same wave, so the prerequisite is not satisfied.
#
# Return whether the deployment plan is valid.
#
# AlgorithmsGraph TheoryArraysLogic
# Solution
def solve(waves: list[list[str]], prerequisites: list[tuple[str, str]]) -> bool:
    package_wave = {}
    for wave_index, wave in enumerate(waves):
        for package in wave:
            if package in package_wave: return False
            package_wave[package] = wave_index
    for package, required in prerequisites:
        if package not in package_wave or required not in package_wave: return False
        if package_wave[required] >= package_wave[package]: return False
    return True