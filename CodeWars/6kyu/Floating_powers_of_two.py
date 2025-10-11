# Write a function that tests if a given floating point number is a power of two, and then calculates the exponent.
#
# For the purposes of this kata, the powers of two are 1, 2, 4, ..., 0.5, 0.25, ..., but also the negative values -1, -2, -4, ..., -0.5, -0.25, ...
#
# If the number is a power of two in this sense, the function should return the exponent: 0 for input 1, 1 for input 2, -1 for 0.5, -2 for 0.25, and so on.
#
# The sign of the number does not matter – the function should return 0 for input -1, 1 for -2, -1 for -0.5, ...
#
# If the number is not a power of two, the function should return the error value NaN (not a number).
#
# The function must only return an exponent if the floating point number exactly represents a power of two.