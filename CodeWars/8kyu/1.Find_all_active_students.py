# Write a simple query to display student information of all active students.
#
# TABLE STRUCTURE:
#
# students
# id (integer)	firstname (text)	lastname (text)	isactive (boolean)
# Sort the results by increasing order of id.
#
# DatabasesSQL
# Solution
SELECT * FROM students
WHERE isactive IS true;