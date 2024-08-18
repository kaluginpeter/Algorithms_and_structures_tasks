# Task
# You need to create a function, helloWorld, that will return the String Hello, World! without actually using raw strings. This includes quotes, double quotes and template strings. You can, however, use the String constructor and any related functions.
#
# You cannot use the following:
#
# "Hello, World!"
# 'Hello, World!'
# `Hello, World!`
# Good luck and try to be as creative as possible!
#
# STRINGSRESTRICTEDPUZZLES
# Solution
def hello_world():
  return chr(72) + chr(101) + chr(108) + chr(108) + chr(111) + chr(44) + chr(32) + chr(87) + chr(111) + chr(114) + chr(108) + chr(100) + chr(33)