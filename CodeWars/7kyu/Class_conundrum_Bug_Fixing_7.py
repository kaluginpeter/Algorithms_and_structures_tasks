# Class conundrum - Bug Fixing #7
# Oh no! Timmy's List Class has broken! Can you help timmy and fix his class? Timmy has a List class he has created, this is used for type strict arrays (which timmy calls Lists).
#
# When timmy calls the Count property of the list it still remains at 0 when adding items.
#
# Also it fails when timmy trys to chain the adds e.g.
#
# my_list.add(0).add(1)
# DEBUGGING
# Solution
class List:
    def __init__(self, list_type):
        self.type = list_type
        self.items = []
        self.count = 0

    def add(self, item):
        if type(item) != self.type:
            return "This item is not of type: {}".format(self.type.__name__)
        self.items.append(item)
        self.count += 1
        return self