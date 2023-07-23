# Given the initial display lines and the rotor moves for each line, determine what the board will say after it has been fully updated.
#
# For your convenience the characters of each rotor are in the pre-loaded constant ALPHABET which is a string.
#
# And don't forget to try my other flap display Katas!
#
# :-)
#
# ALGORITHMS
# Solution
def flap_display(lines, rotors):
    word, steps, out = '', [], []
    al = ALPHABET + ALPHABET
    for i in rotors:
        top = []
        for j in range(len(i) + 1):
            top.append(sum(i[:j + 1]))
        steps.append(top)
    for j in range(len(lines)):
        for i in range(len(lines[j])):
            if steps[j][i] > len(ALPHABET):
                steps[j][i] = steps[j][i] % len(ALPHABET)
            word += al[al.index(lines[j][i]) + steps[j][i]]
        out.append(word)
        word = ''
    return out