# Prolog:
# This kata series was created for friends of mine who just started to learn programming. Wish you all the best and keep your mind open and sharp!
#
# Task:
# Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.
#
# Examples:
# 42, "int"    --> True
# "42", "int"  --> False
# FUNDAMENTALS
# Solution
def type_validation(variable, _type):
    return _type in str(type(variable))