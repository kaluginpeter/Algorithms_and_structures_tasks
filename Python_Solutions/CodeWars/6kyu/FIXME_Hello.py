# The code provided has a method hello which is supposed to show only those
# attributes which have been explicitly set. Furthermore, it is supposed to say them in the same order they were set.
#
# But it's not working properly.
#
# Notes
# There are 3 attributes
#
# name
# age
# sex ('M' or 'F')
# When the same attribute is assigned multiple times the hello method shows it only once.
# If this happens the order depends on the first assignment of that attribute,
# but the value is from the last assignment.
#
# Examples
# Hello.
# Hello. My name is Bob. I am 27. I am male.
# Hello. I am 27. I am male. My name is Bob.
# Hello. My name is Alice. I am female.
# Hello. My name is Batman.
# Task
# Fix the code so we can all go home early.
#
# DEBUGGING
# Solution
class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.hell = 'Hello.'

    def setAge(self, age):
        if self.age == None:
            self.hell = self.hell + ' I am {age}.'
        self.age = age
        return self

    def setSex(self, sex):
        if self.sex == None:
            self.hell = self.hell + ' I am {sex}.'
        self.sex = "male" if sex == 'M' else "female"
        return self

    def setName(self, name):
        if self.name == None:
            self.hell = self.hell + ' My name is {name}.'
        self.name = name
        return self

    def hello(self):
        return self.hell.format(age=self.age, sex=self.sex, name=self.name)