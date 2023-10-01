# It's important day today: the class has just had a math test. You will be given a list of marks. Complete the function that will:
#
# Calculate the average mark of the whole class and round it to 3 decimal places.
# Make a dictionary/hash with keys "h", "a", "l" to make clear how many high, average and low marks they got. High marks are 9 & 10, average marks are 7 & 8, and low marks are 1 to 6.
# Return list [class_average, dictionary] if there are different type of marks, or [class_average, dictionary, "They did well"] if there are only high marks.
# Examples
# [10, 9, 9, 10, 9, 10, 9] ==> [9.429, {'h': 7, 'a': 0, 'l': 0}, 'They did well']
#
# [5, 6, 4, 8, 9, 8, 9, 10, 10, 10] ==> [7.9, {'h': 5, 'a': 2, 'l': 3}]
# FUNDAMENTALSLISTS
# Solution
def test(r):
    avr = round(sum(r)/len(r), 3)
    h, a, l = 0, 0, 0
    for mark in r:
        if 9 <= mark <= 10:
            h += 1
        elif 7 <= mark <= 8:
            a += 1
        elif 1 <= mark <= 6:
            l += 1
    l = [avr, {'h': h, 'a': a, 'l': l}, f"{'They did well' if a + l == 0 else ''}"]
    return l[:-1] if l[-1] == '' else l