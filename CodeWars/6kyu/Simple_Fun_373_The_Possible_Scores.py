# Problem
# John and Tom are students of Myjinxin.
#
# In the classroom, Myjinxin often gives 10 judgment questions, let the students write the answer. o represents right and x represents wrong. i.e. If the students think that the 10 judgments are all right, his answer will be "oooooooooo".
#
# Tom always answers questions earlier than John. Then, the teacher gives Tom a score, each subject worth 10 points. i.e. If Tom's answer is "oooooooooo" and the correct answer is "ooxxxxxxxx", Tom got 20 points.
#
# John didn't know what the correct answer was. He has his own answer.
#
# John looked at Tom's answer and Tom's score, and he wanted to know what the minimum possible score and the maximum possible score he could get..
#
# Task
# You are given three arguments:
#
# answerOfTom: Tom's answer. It's a string of length 10, contains only o or x.
#
# scoreOfTom: Tom's score. an integer that can be 0,10,20,...,100.
#
# answerOfJohn: John's answer. It's a string of length 10, contains only o or x.
#
# Your result should be a 2-elements integer array/tuple: <minimum possible score of John>, <maximum possible score of John>
#
# Still not understand the task? Look at the following example ;-)
#
# Examples
# For answerOfTom="oooooooooo", scoreOfTom=20, answerOfJohn="oooooooooo" the output should be 20,20
#
# In this case, John's answer is same as Tom's, so his scores can only be 20.
#
# For answerOfTom="oooooooooo", scoreOfTom=20, answerOfJohn="xxxxxxxxxx" the output should be 80,80
#
# In this case, John's answer is just the opposite of Tom's, so his scores can only be 80.
#
# For answerOfTom="oooooooooo", scoreOfTom=20, answerOfJohn="oooooxxxxx" the output should be 30,70
#
# In this case, Tom's score is 20. It means two questions Tom answered correctly.
#
# Let's think about some situations:
#
# If the first question and second question Tom answered correctly, the whole correct answer may be "ooxxxxxxxx", John will get 70 points;
#
# If the last question and second last question Tom answered correctly, the whole correct answer may be "xxxxxxxxoo", John will get 30 points;
#
# If the 5th question and 6th question Tom answered correctly, the whole correct answer may be "xxxxooxxxx", John will get 50 points;
#
# ...and other situations...
#
# So, John can get at least 30 points, at most 70 points.
#
# Note
# Happy Coding ^_^
# FUNDAMENTALS
# Solution
def possible_scores(answer_of_tom, score_of_tom, answer_of_john):
    x: int = sum(i != j for i, j in zip(answer_of_tom, answer_of_john))
    ans: int = None
    n: int = score_of_tom // 10
    if x == 0:
        ans = n
    elif x == 10:
        ans = x - n
    else:
        ans = min(10 - x + (10 - n), x + n)
    return (abs(x - n) * 10, ans * 10)