# Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?
# Well, here you have to calculate how many keystrokes you have to do for a specific word.
#
# This is the layout:
#
#
# Given a string, return the number of keystrokes necessary to type it. You can assume that the input will entirely consist of characters included in the mobile layout (lowercase letters, digits, and the symbols * and #).
#
# Examples
# "*#"       =>  2 (1 + 1)
# "123"      =>  3 (1 + 1 + 1)
# "abc"      =>  9 (2 + 3 + 4)
# "codewars" => 26 (4 + 4 + 2 + 3 + 2 + 2 + 4 + 5)
# Fundamentals
# Solution
def mobile_keyboard(s):
    words: list[str] = [' abc', ' def', ' ghi', ' jkl', ' mno', ' pqrs', ' tuv', ' wxyz', '*', '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    output: int = 0
    for char in s:
        for keystroke in words:
            if char in keystroke: output += keystroke.index(char) + 1
    return output