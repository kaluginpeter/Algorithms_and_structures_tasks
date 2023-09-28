# Task
# Write the processArray function, which takes an array and a callback function as parameters. The callback function can be, for example, a mathematical function that will be applied on each element of this array. Optionally, also write tests similar to the examples below.
#
# Examples
# Array [4, 8, 2, 7, 5] after processing with function
#
# function(a): return a*2;
# will be [ 8, 16, 4, 14, 10 ].
#
# Array [7, 8, 9, 1, 2] after processing with function
#
# function(a): return a+5;
# will be [ 12, 13, 14, 6, 7 ].
#
# ALGORITHMS
# Solution
def process_array(arr, callback):
    return [callback(i) for i in arr]