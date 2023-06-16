# It might be déjà vu, or it might be a duplicate day.
# You’re well trained in the arts of cleaning up duplicates.
# Someone has hacked your database and injected all kinds of duplicate
# records into your tables. You don’t have access to modify the data in
# the tables or restore the tables to a previous time because the DBA’s are gone.
#
# You are provided with an array of employees from the server.
# Your task is to write the findDuplicates function to remove
# the duplicate records after they are sent down to the client.
#
# Employee Class:
#
# class Employee:
#   def __init__(self,f_name,l_name,u_name):
#     self.first_name = f_name
#     self.last_name = l_name
#     self.user_name = u_name
# The result of calling the findDuplicates function should be an array of the
# Employee objects that are the duplicates. findDuplicates should also perform
# an in place modification of the array it's given (employees), removing the duplicate values.
#
# Assumptions:
#
# You can assume that the employees parameter passed in to findDuplicates is always an array.
# You can also assume that the employees array is a flat array.
# ALGORITHMS
# Solution
def find_duplicates(emp):
    l, l1, s = [], [], set()
    for i in emp:
        if i in s: l.append(i)
        else: l1.append(i); s.add(i)
    emp.clear()
    emp.extend(l1)
    return l