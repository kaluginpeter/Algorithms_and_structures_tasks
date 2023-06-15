# Consider an array containing cats and dogs.
# Each dog can catch only one cat, but cannot catch a cat that is more than n elements away.
# Your task will be to return the maximum number of cats that can be caught.
#
# For example:
#
# solve(['D','C','C','D','C'], 2) = 2, because the dog at index 0 (D0) catches C1 and D3 catches C4.
# solve(['C','C','D','D','C','D'], 2) = 3, because D2 catches C0, D3 catches C1 and D5 catches C4.
# solve(['C','C','D','D','C','D'], 1) = 2, because D2 catches C1, D3 catches C4. C0 cannot be caught because n == 1.
# solve(['D','C','D','D','C'], 1) = 2, too many dogs, so all cats get caught!
# Do not modify the input array.
#
# More examples in the test cases. Good luck!
#
# ALGORITHMS