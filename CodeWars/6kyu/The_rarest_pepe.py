# The pepe market is on the verge of collapse. In a last-ditch attempt to make some quick cash, you decide to sift through the thousands of pepes on the internet to identify the rarest ones, which are worth more. Since doing this by hand would be tedious, you decide to use your programming skills to streamline the process.
#
# Your task in this kata is to implement a function that, given a non-empty list of pepes (pepes), returns the rarest pepe in the list.
#
# If two or more pepes are equally rare, return a sorted list of these pepes.
# If the rarest pepe (or pepes) has a frequency of 5 or more, then there are no truly rare pepes, so your function should return "No rare pepes!".
# More info on rare pepes here.
#
# Algorithms
# Solution
def find_rarest_pepe(pepes):
    hashmap: dict[str, int] = dict()
    for pepe in pepes:
        hashmap[pepe] = hashmap.get(pepe, 0) + 1
    if (bound := min(hashmap.values())) >= 5:
        return 'No rare pepes!'
    output: list[str] = sorted([pepe for pepe in hashmap if hashmap[pepe] == bound])
    if len(output) == 1: return output[0]
    return output