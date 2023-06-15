# You must create a method that can convert a string from any format into PascalCase. This must support symbols too.
#
# Don't presume the separators too much or you could be surprised.
#
# For example: (Input --> Output)
#
# "example name" --> "ExampleName"
# "your-NaMe-here" --> "YourNameHere"
# "testing ABC" --> "TestingAbc"
# STRINGSALGORITHMS
# Solution
import re
def camelize(s):
    return "".join(i.capitalize() for i in re.split("\W|_", s))