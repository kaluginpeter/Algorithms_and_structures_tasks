# There exists a sequence of numbers that follows the pattern
#
#           1
#          11
#          21
#         1211
#        111221
#        312211
#       13112221
#      1113213211
#           .
#           .
#           .
# Starting with "1" the following lines are produced by "saying what you see", so that line two is "one one", line three is "two one(s)", line four is "one two one one".
#
# Write a function that given a starting value as a string, returns the appropriate sequence as a list. The starting value can have any number of digits. The termination condition is a defined by the maximum number of iterations, also supplied as an argument.
#
# RECURSIONALGORITHMS
# Solution
def look_and_say(data='1', maxlen=5):
    ans: list = list()
    for i in range(maxlen):
        top: str = ''
        prev: str = ans[-1][0]  if ans else data[0]
        count: int = 1
        for j in range(1, len(ans[-1]) if ans else len(data)):
            if prev != (ans[-1][j] if ans else data[j]):
                top += str(count) + prev
                count, prev = 1, ans[-1][j] if ans else data[j]
            else:
                count += 1
        if count > 0:
            top += str(count) + prev
        ans.append(top)
    return ans