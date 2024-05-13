# Make me slow! Calling makeMeSlow() should take at least 7 seconds.
#
# FUNDAMENTALS
# Solution
import time
def make_me_slow():
    time.sleep(7)
    for i in range(1000000):
        pass