# You just took a contract with the Jedi council. They need you to write a function, greet_jedi(), which takes two arguments (a first name and a last name), works out the corresponding Jedi name, and returns a string greeting the Jedi.
#
# A person's Jedi name is the first three letters of their last name followed by the first two letters of their first name. For example:
#
# >>> greet_jedi('Beyonce', 'Knowles')
# 'Greetings, master KnoBe'
# Note the capitalization: the first letter of each name is capitalized. Your input may or may not be capitalized. Your function should handle it and return the Jedi name in the correct case no matter what case the input is in:
#
# >>> greet_jedi('grae', 'drake')
# 'Greetings, master DraGr'
# You can trust that your input names will always be at least three characters long.
#
# If you're stuck, check out the python.org tutorial section on strings and search "slice".
#
# FUNDAMENTALS
# Solution
def greet_jedi(first, last):
    return f'Greetings, master {last[:3].title() + first[:2].title()}'