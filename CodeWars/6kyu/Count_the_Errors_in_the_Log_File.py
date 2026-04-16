# Congratulations! You just deployed your company's first server!
# Unfortunately, it has a lot of problems, and your boss is very upset about this. He wants you to gather every single error from the log file and send it to him. Since he needs it by the end of the day, you must write code to do this, otherwise you will never finish on time, and could even get fired! To do a favor to the development team who will probably just receive the list of errors from your inconsiderate boss as you give it to him, you must sort the list by number of occurrences, from highest to lowest.
#
# Problem
# There is a file named server.log which contains all activity on the server, including errors. You must search through this file and return a map with every error and its number of occurrences.
#
# In Python:
# Return a dict[str, int].
# Constraints
# The file will always be called "server.log" exactly and will always contain at least one error (otherwise why are you doing this). The file will always exist.
#
# Every line of the file is its own event, so no line of the file will have multiple errors.
#
# Each error will start with "ERROR: " exactly, and no lines will have "ERROR: " without anything after. "ERROR: " should only be counted if it is fully uppercase.
#
# All errors are case insensitive and should be stored fully lowercase without "ERROR: ".
#
# If anything comes before "ERROR: " the error should be ignored and not counted.
#
# Order does not matter for errors that occur the same amount of times.
#
# Example
# server.log:
# Event1
# ERROR: eRRor1
# ERROR: ERRor2
# ERROR: ErRor2
# ERROR: ErROr1
# ERROR: Error3
# ERROR: ErrOr2
# ERROR: ErroR3
# ERROR: ERRoR5
# ERROR: Error1
# ERROR: errOr5
# ERROR: ErRor4
# Event2
# Event2
# Event3 ERROR: error2
# ERROR: eRrOR1
# Event1
# Err: error4
# error: error4
# ErROr: error4
# Output:
# {'error1': 4, 'error2': 3, 'error3': 2, 'error5': 2, 'error4': 1}
# # error3 and error5 could be in any order
# Test Cases
# The file will have at most 200 lines
# There will always be at least one valid error in a file
# The file will always exist and be valid, and will always be named server.log
# Order will NEVER be checked for elements that occur the same amount of times
# Order will ALWAYS be checked for elements that occur a different amount of times
# There will be 5 fixed tests and 5 random tests
# Good Luck!
# Solution
from collections import defaultdict

def map_errors():
    output: dict[str, int] = defaultdict(int)
    with open("server.log") as f:
        for line in f:
            try:
                output[line.split(": ")[1].lower().strip()] += 1
            except: continue
    return dict(sorted(output.items(), reverse=True, key=lambda p: p[1]))