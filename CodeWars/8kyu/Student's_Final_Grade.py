# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.
#
# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);
#
# This function should return a number (final grade). There are four types of final grades:
#
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases
# Examples(Inputs-->Output):
#
# 100, 12 --> 100
# 99, 0 --> 100
# 10, 15 --> 100
#
# 85, 5 --> 90
#
# 55, 3 --> 75
#
# 55, 0 --> 0
# 20, 2 --> 0
# *Use Comparison and Logical Operators.
#
# FUNDAMENTALS
# Solution
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0