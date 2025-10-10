# Build up a method that takes a positive integer and formats it to a 'time - like' format.
#
# The method must raise an exception if its hour length is less than 3 digits and greater than 4.
#
# Examples:
# 800   --> '8:00'
# 1000  --> '10:00'
# 1451  --> '14:51'
# 3351  --> '33:51'
# 10000 --> raise an exception
# StringsFundamentals
# Solution
def solution(hour):
    x: str = str(hour)
    if len(x) > 4 or len(x) <= 2: raise Exception()
    if len(x) == 3:
        return x[0] + ':' + x[1:]
    return x[:2] + ':' + x[2:]