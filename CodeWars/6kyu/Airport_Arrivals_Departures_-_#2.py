# Well here you are again, still staring blankly at the same arrivals/departures flap display...
#
# Kata Task
# Part #1
# In Part #1 of this series you already figured out how the flap display mechanism works.
#
# You now know what the updated display will look like after applying a set of rotor moves.
#
# If you haven't already completed Part 1, then now is a good time to do it!
#
# Part #2
# Now in this current Kata your task is the opposite.
#
# It's the same board with the same rules...
#
# But this time you are required to return the set of rotor moves needed to
# transform the display from the before to the after state.
#
# Look at the example tests for guidance.
#
# And good luck!
#
# :-)
#
# Notes
# For Java and C#, a convenient String of the rotor characters provided in Preloaded.ALPHABET
# ALGORITHMS
# Suggest kata description edits
# Solution
def flat_rotors(lines_before, lines_after):
    ln = len(ALPHABET)
    def nxt_rotor(wb, wa):
        l = []
        for i,j in zip(wb, wa):
            l.append((ALPHABET.index(j) - ALPHABET.index(i) - sum(l)) % ln)
        return l
    return [nxt_rotor(i,j) for i,j in zip(lines_before, lines_after)]