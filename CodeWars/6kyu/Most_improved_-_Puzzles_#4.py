# Most Improvd - Puzzles #4
# When being graded in a subject or a course high marks are focused on the most but what about
# most improved? As a computer science teacher you would like to create a
# function which calculates the most improved students and rank them in a list.
#
# Task
# Your task is to compelete the function calculateImproved to return an array sorted by most improved as percentages.
#
# Input
# The input you will receive will be an array of students, students will be an object containing
# a name and array of marks (in order of acheived) the marks will be out of 100, a student can
# however have a mark of null if the test was not attempted (treat this as 0)
# Example of student Object: ```{name:'Henry, Johns',marks:[25,50]}```
#
# Output
# The output expected will be an array of objects similar to the student object, containing
# the name and total improvement percentage out of the first and last mark given to calculate
# the overall improvement percentage. The output array must be sorted by most improved
# (Round the calculated improvement) If there is a tie in improvements then order by name (capitals before lowercase).
# Example of return Object: ```{name:'Henry, Johns',improvement:100}```
#
# Preloaded
# The Student class has been preloaded with the constructor accepting two parameters a
# name and marks which should be an array of numbers.
#
# ARRAYSPUZZLES
# Solution
def calculate_improved(students):
    for i in students: i['marks'] = [j if j != None else 0 for j in i['marks']]
    l = [{'name': i['name'], 'improvement': round((i['marks'][-1]-i['marks'][0])*100/i['marks'][0]) if i['marks'][0] else 0} for i in students]
    return sorted(l, key=lambda x: (-x['improvement'], x['name'][0].islower(), x['name']))