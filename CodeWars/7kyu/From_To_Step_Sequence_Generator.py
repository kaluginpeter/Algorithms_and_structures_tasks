# Write a function that generate the sequence of numbers which starts from the "From" number, then adds to each next term the "Step" number until the "To" number. For example:
#
# generator(10, 20, 10) = [10, 20] # "From" = 10, "Step" = 10, "To" = 20
# generator(10, 20, 1) = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# generator(10, 20, 5) = [10, 15, 20]
# If next term is greater than "To", it can't be included into the output array:
#
# generator(10, 20, 7) = [10, 17]
# If "From" bigger than "To", the output array should be written in reverse order:
#
# generator(20, 10, 2) = [20, 18, 16, 14, 12, 10]
# Don't forget about input data correctness:
#
# generator(20, 10, 0) = []
# generator(10, 20, -5) = []
# "From" and "To" numbers are always integer, which can be negative or positive independently. "Step" can always be positive.
#
# ArraysFundamentals