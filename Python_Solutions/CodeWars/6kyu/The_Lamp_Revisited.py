# Define a class called Lamp. It will have a string attribute for color and boolean attribute, on, that will refer to whether the lamp is on or not. Define your class constructor with a parameter for color and assign on as false on initialize.
#
# Give the lamp an instance method called toggle_switch that will switch the value of the on attribute.
#
# Define another instance method called state that will return "The lamp is on." if it's on and "The lamp is off." otherwise.
#
# FUNDAMENTALS
# Solution
class Lamp():
    def __init__(self, color, on=False):
        self.color = color
        self.on = on
    def toggle_switch(self):
        self.on = not self.on
    def state(self):
        return 'The lamp is on.' if self.on else 'The lamp is off.'