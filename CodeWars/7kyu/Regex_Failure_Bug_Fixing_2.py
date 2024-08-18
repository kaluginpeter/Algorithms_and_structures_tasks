# Problem Description:
#
# Oh no, Timmy's received some hate mail recently but he knows better. Help Timmy fix his regex filter so he can be awesome again!
#
# Task:
#
# You are given a string phrase containing some potentially offensive words such as "bad," "mean," "ugly," "horrible," and "hideous." Timmy wants to replace these words with the word "awesome" to make the message more positive. Your task is to implement a function, that replaces all occurrences of these offensive words with "awesome" in the input string phrase.
#
# Input:
#
# A string phrase containing words separated by spaces.
# Output:
#
# A string with the same words as phrase, but with any offensive words replaced by "awesome."
# Example:
#
# Input: "You're Bad! timmy!"
# Output: "You're awesome! timmy!"
# Input: "You're MEAN! timmy!"
# Output: "You're awesome! timmy!"
# DEBUGGING
# Solution
import re
def filter_words(phrase):
    return re.sub("(bad|mean|ugly|horrible|hideous)","awesome", phrase, flags=re.IGNORECASE)