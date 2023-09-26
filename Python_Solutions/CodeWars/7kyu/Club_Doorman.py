# INTRODUCTION
# The Club Doorman will give you a word. To enter the Club you need to provide the right number according to provided the word.
#
# Every given word has a doubled letter, like 'tt' in lettuce.
#
# To answer the right number you need to find the doubled letter's position of the given word in the alphabet and multiply this number per 3.
#
# It will be given only words with one doubled letter.
#
#
# EXAMPLE
#
# Lettuce is the given word. 't' is the doubled letter and it's position is 20 in the alphabet.
#
#
# The answer to the Club Doorman is 20 * 3 = 60
#
#
# TASK
# The function passTheDoorMan with a given string word shall return the right number.
#
# FUNDAMENTALS
# Solution
def pass_the_door_man(word):
    for char in word:
        if char*2 in word:
            return (ord(char)-96) * 3