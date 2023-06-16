# Would you believe me if I told you these particular tuples are special?
#
# (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31)
#
# (2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31)
#
# (4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31)
#
# (8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31)
#
# (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
#
# You want to know why? Ok, I'll tell you:
#
# If you think of a number, between 1 and 31, I can tell what number you are thinking,
# just by asking you in which tuple you can find that number. You don't believe me? What if I tell you the trick?
#
# This is the trick:
#
# sum all the first elements of the tuples where you can find the number you are thinking of.
# If you do it correctly you will get your number.
# So for example, let's say I am thinking about the number 5. It can be found in the first and third tuple,
# which have respectively the numbers 1 and 4 as first element. The sum of 1 and 4 is 5!
#
# You don't believe me yet? Maybe you think it only works for the number 5. Try it for yourself, so that we
# can continue our journey. I'll wait.
#
# ........
#
# Did it work? Of course it did! This is know as "Brown's Criterion". It works for all numbers from 1 to 31.
#
# Your task is to create two functions:
#
# The first one is called "guess_number", it gives you a list of answers. These answers can be integers
# values (1 or 0), and correspond respectively to Yes and No. The sequence values are the answer
# to "Do you see your number?" for each one of the above tuples. You are given the sequence and
# must return the number which originated that sequence of answers.
# Example: for the sequence [1, 0, 1, 0, 0] you must return the number 5.
# The second one is called "answers_sequence". It is the exact opposite of the first function.
# You are given a number and must return the sequence of answers for that number.
# -------------------------------------- Notes ----------------------------------------
#
# The argument for the function "Guess_Number" will always be a list;
# The argument for the function "Answers_Sequence" will always be a number;
# Good Luck!
#
# MATHEMATICSLOGICPUZZLES
# Solution
sequence = ((1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31),
            (2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31),
            (4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31),
            (8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31),
            (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))


def guess_number(answers):
    return sum(sequence[i][0] for i in range(len(answers)) if answers[i] == 1)

def answers_sequence(n):
    return [1 if n in i else 0 for i in sequence]