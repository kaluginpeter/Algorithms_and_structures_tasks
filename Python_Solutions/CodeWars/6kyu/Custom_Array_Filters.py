# Dave has a lot of data he is required to apply filters to,
# which are simple enough, but he wants a shorter way of doing so.
#
# He wants the following functions to work as expected:
#
# even # list([1,2,3,4,5]).even() should return [2,4]
# odd # list([1,2,3,4,5]).odd() should return [1,3,5]
# under # list([1,2,3,4,5]).under(4) should return [1,2,3]
# over # list([1,2,3,4,5]).over(4) should return [5]
# in_range # list([1,2,3,4,5]).in_range(1, 3) should return [1,2,3]
# They should also work when used together, for example:
#
# list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) # should return [2,4]
# And finally the filters should only accept integer values from an array, for example:
#
# list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() // should return [300, 122]
# Note: List with non-numbers will be tested as well.
#
# ARRAYSFUNDAMENTALS
# Solution
class list(list):
    def even(self):
        res = []
        for x in self:
            if type(x) == int and x % 2 == 0:
                res.append(x)
        return res
    def odd(self):
        res = []
        for x in self:
            if type(x) == int and x % 2 == 1:
                res.append(x)
        return res
    def under(self, r):
        res = []
        for x in self:
            if type(x) == int and x < r:
                res.append(x)
        return res
    def over(self, r):
        res = []
        for x in self:
            if type(x) == int and x > r:
                res.append(x)
        return res
    def in_range(self, r1, r2):
        res = []
        for x in self:
            if type(x) == int and r1 <= x <= r2:
                res.append(x)
        return res