# Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.
#
# Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:
#
# q1 is our start state, we begin reading commands from here
# q2 is our accept state, we return true if this is our last state
# And the transitions:
#
# q1 moves to q2 when given a 1, and stays at q1 when given a 0
# q2 moves to q3 when given a 0, and stays at q2 when given a 1
# q3 moves to q2 when given a 0 or 1
# The automaton should return whether we end in our accepted state (q2), or not (true/false).
#
# Your task
# You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2, and q3 for the myAutomaton instance. The test fixtures will be calling against myAutomaton.
#
# As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'
#
# Here are some resources on DFAs (the automaton this Kata asks you to create):
#
# http://en.wikipedia.org/wiki/Deterministic_finite_automaton
# http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html
# http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf
# Example
# a = Automaton()
# a.read_commands(["1", "0", "0", "1", "0"])  ==> False
# We make these transitions:
#
# input: ["1", "0", "0", "1", "0"]
#
# 1: q1 -> q2
# 0: q2 -> q3
# 0: q3 -> q2
# 1: q2 -> q2
# 0: q2 -> q3
# We end in q3 which is not our accept state, so we return false
#
# STATE MACHINESARTIFICIAL INTELLIGENCEALGORITHMSOBJECT-ORIENTED PROGRAMMING
# Solution
class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        start = self.states[0]
        for i in commands:
            if start == self.states[0]:
                start = self.states[1] if i == '1' else self.states[0]
            elif start == self.states[1]:
                start = self.states[2] if i == '0' else self.states[1]
            else:
                start = self.states[1] if i in '01' else self.states[2]
        return start == 'q2'
my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.
my_automaton.states.append('q1')
my_automaton.states.append('q2')
my_automaton.states.append('q3')