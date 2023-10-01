# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
#
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!
#
# LISTSARRAYSFUNDAMENTALS
# Solution
def remove_every_other(my_list):
    del my_list[1::2]
    return my_list