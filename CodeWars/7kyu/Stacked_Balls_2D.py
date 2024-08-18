# Background
# I have stacked some pool balls in a triangle.
#
# Like this,
#
# pool balls
# Kata Task
# Given the number of layers of my stack, what is the total height?
#
# Return the height as multiple of the ball diameter.
#
# Example
# The image above shows a stack of 5 layers.
#
# Notes
# layers >= 0
# approximate answers (within 0.001) are good enough
# See Also
#
# Stacked Balls - 2D
# Stacked Balls - 3D with square base
# Stacked Balls - 3D with triangle base
# FUNDAMENTALS
# Solution
def stack_height_2d(layers):
    if layers in {0, 1}:
        return layers
    return 1 + (layers - 1) * 0.8660254