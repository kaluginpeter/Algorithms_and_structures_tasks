# Groups of characters decided to make a battle. Help them to figure out what group is more powerful. Create a function that will accept 2 variables and return the one who's stronger.
#
# Rules
# Each character has its own power:
#   A = 1, B = 2, ... Y = 25, Z = 26
#   a = 0.5, b = 1, ... y = 12.5, z = 13
# Only alphabetical characters can and will participate in a battle.
# Only two groups to a fight.
# Group whose total power (a + B + c + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples
# "One", "Two"  -->  "Two"
# "ONE", "NEO"  -->  "Tie!"
# Related kata
# Battle of the characters (Easy)
# ALGORITHMS
# Solution
def battle(первое_слово: str, второе_слово: str) -> str:
    алфавит = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    сумма_первого_слова = sum(алфавит.index(буква)+1 if буква.isupper() else (алфавит.index(буква.upper())+1)/2 for буква in первое_слово)
    сумма_второго_слова = sum(алфавит.index(буква)+1 if буква.isupper() else (алфавит.index(буква.upper())+1)/2 for буква in второе_слово)
    return первое_слово if сумма_первого_слова > сумма_второго_слова else второе_слово if сумма_второго_слова > сумма_первого_слова else 'Tie!'