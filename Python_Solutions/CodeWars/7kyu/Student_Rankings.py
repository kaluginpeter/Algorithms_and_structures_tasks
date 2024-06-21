# Often times in schools, at the end of a semester or term, the teacher or professor will post the grades publically for everyone to see the day after the finals. Students can go to a public bulletin and check their grades to see how they did on an exam and where their ranking stands. This kata, Student Rankings will have you, the professor automate the list making for the many classes you're in charge of!
#
# Input
# Your function `post_grades` will receive a list of students denoted as *students*.
# example_student_list = [
#   'S01 - Student Name A - 95 98.4 92.15',
#   'S02 - Student Name B - 100 96.4 90',
#   'S03 - Student Name C - 84.2 90.5 92.8',
#   'S04 - Student Name D - 80 96.4 88.4'
# ]
# Each student will have three things split by the - character:
#
# A student id i.e. S01
# A student name i.e. Student Name A
# A list of grades separated by spaces i.e. 95 98.4 92.15
# To make it easy for the professor, each student will be represented as a single string.
#
# Output
# Write a function `post_grades(students)` that returns a sorted list of pairs containing the `student id` and the `average score`. So for the example list provided, the output would look like the following:
# result = [('S02',95.47),('S01',95.18),('S03',89.17),('S04',88.27)]
# Notes:
#
# For an empty list, return the empty list []
# The list should sort from highest average score to lowest average score i.e. 100 -> 0
# FUNDAMENTALS
# Solution
def post_grades(students):
    output = []
    for stud in students:
        id_, name, score = stud.split('-')
        score = list(map(float, score[1:].split()))
        output.append((id_[:-1], sum(score) / len(score)))
    return sorted(output, key=lambda x: x[1], reverse=True)