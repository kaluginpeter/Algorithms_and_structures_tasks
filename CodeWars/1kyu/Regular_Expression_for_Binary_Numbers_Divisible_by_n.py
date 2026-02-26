# Regular Expression for Binary Numbers Divisible by n
# Create a function that will return a regular expression string that is capable of evaluating binary strings (which consist of only 1s and 0s) and determining whether the given string represents a number divisible by n.
#
# Tests
# Inputs 1 <= n <= 18 will be tested
#
# Each n will be tested against random invalid tests and random valid tests (which may or may not pass the regex test itself, accordingly).
#
# Notes
# Strings that are not binary numbers should be rejected.
# Keep your solution under 5000 characters. This means you can't hard-code the answers.
# Only these characters may be included in your returned string:
# 01?:*+^$()[]|
#
# C++ Notes
# The second anti-cheat test checks if you used the STL's regex library in your code.
# The macro constant _GLIBCXX_REGEX_STATE_LIMIT which limits the maximum size of a regex has been set to 400000, as the default limit would be too constraining for the larger inputs.
# AlgorithmsPuzzlesRegular ExpressionsStrings
# Solution
E = 'e'

class State():
    def __init__(self, number, prior_state = [], post_state = []):
        self.id = number
        self.prior_state = prior_state
        self.post_state = post_state

def initStatesArches(number):
    states = []
    for i in range(number): states.append(State(i, [], []))
    arches = [[None for i in range(number)] for j in range(number)]
    for i in range(number):
        addArch(states, arches, i, i * 2 % number, '0')
        addArch(states, arches, i, (i * 2 + 1) % number, '1')
    return states, arches

def addArch(states, arches, begin, end, string):
    if begin != end:
        states[begin].post_state.append(end)
        states[end].prior_state.append(begin)
    arches[begin][end] = string

def deleteArch(state, is_prior, value):
    lista =  state.prior_state if is_prior else state.post_state
    if value not in lista: return
    lista.remove(value)

def reduceState(states, arches, cur_state):
    for origin in cur_state.prior_state:
        for goal in cur_state.post_state:
            pre_state = states[origin]
            pos_state = states[goal]
            arch_origin_goal = arches[origin][goal]
            arch_origin_cur = arches[origin][cur_state.id]
            arch_cur_goal = arches[cur_state.id][goal]
            arch_cur_cur = arches[cur_state.id][cur_state.id]
            if arch_cur_cur:
                if len(arch_cur_cur) > 1: term = '(?:{})*'.format(arch_cur_cur)
                else: term = '{}*'.format(arch_cur_cur)
            else: term = E
            half_exp = addExp(arch_origin_goal, concatExp(arch_origin_cur, term, arch_cur_goal))
            deleteArch(pre_state, False, pos_state.id)
            deleteArch(pos_state, True, pre_state.id)
            addArch(states, arches,  pre_state.id, pos_state.id, half_exp)
            deleteArch(pre_state, False, cur_state.id)
            deleteArch(pos_state, True, cur_state.id)

def addExp(*args):
    not_E_not_empty = [term for term in args if term and term != E]
    return cleverJoin(not_E_not_empty, '|')

def concatExp(*args):
    not_E = [term for term in args if term != E]
    has_empty_set = False in args
    return '' if has_empty_set else cleverJoin(not_E, '')

def cleverJoin(expression, sep):
    if len(expression) == 1:  return expression[0]
    return sep.join(['(?:{})'.format(term) if '|' in term else term for term in expression])

def regex_divisible_by(n):
    if n == 1: return '^(0|1)+$'
    states, arches = initStatesArches(n)
    for state in states:
        if state.id is not 0: reduceState(states, arches, state)
    expression = arches[0][0]
    return '^(?:{})+$'.format(expression)