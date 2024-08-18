# You're playing to scrabble. But counting points is hard.
#
# You decide to create a little script to calculate the best possible value.
#
# The function takes two arguments :
#
# `points` : an array of integer representing for each letters from A to Z the points that it pays
# `words` : an array of strings, uppercase
#
# You must return the index of the shortest word which realize the highest score.
# If the length and the score are the same for two elements, return the index of the first one.
#
# ARRAYSALGORITHMS
# Solution
def get_best_word(points, words):
    return max(range(len(words)), key=lambda i: (sum(points[ord(j)-65] for j in words[i]), -len(words[i]), -i))