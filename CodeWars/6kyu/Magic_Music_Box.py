# Introduction
# You are on a party with your friends and one of them suggest to play a game called "Magic Music Box". The game consists of a magic music box that is playing one by one all the music notes in order from DO to SI over and over. The goal of the game is to store in the magic music box words that contain the musical note that is being played at each moment.
#
# Music Box
#
# Task
# In this kata you have to create a function that given an array of words returns another array with all the words that have been stored in the magic music box in the correct order.
#
# A word can be stored in the magic music box when it contains the musical note that the box is playing at each moment. When a word is stored, the music box starts to play the next note, and so on.
#
# The function must try to store every word from the input if possible, even if it means to retry some words that didn't fitted previuosly.
#
# If there are no more words in the input that can be stored in the box, the function should stop and return the array with the stored words in the order they have been stored.
#
# Rules
# The same word cannot be stored more than once.
# The magic music box plays the musical notes over and over, in a cyclic infinite loop.
# If a word cannot be stored, it does not mean it could not be stored in the future with the appropiate note.
# You don't have to verify the word, you only have to check that it contains the musical note with all its letters together (i.e. SOLAR would be a valid word but SOCIAL wouldn't).
# The musical notes are represented in the european solfège format (DO, RE, MI, FA, SOL, LA, SI).
# The method must return an empty array if there are no words present inside the array.
# Example
# Given the input array ["DOWN","PLANE","AMIDST","REPTILE","SOFA","SOLAR","SILENCE","DOWN","MARKDOWN"]
#
# The function flow should be:
#
# As the first musical note is DO, the word DOWN fits, and is stored inside the box.
#
# The next note is RE, and iterating the array, the next word that fits is REPTILE.
#
# The next note is MI, but if we continue in the array, we don't find any word that fits, so we should try again from the begining. This time, we find AMIDST, which fits.
#
# The flow continues like this for the next musical notes (FA, SOL, LA, SI). At this point, our temporal resulted array looks like this: ["DOWN", "REPTILE", "AMIDST", "SOFA", "SOLAR", "PLANE", "SILENCE"]
#
# The next note is DO again, because the music box never stops playing notes. Following the array, we find the word DOWN. The word itself fits with the note, but as long as it is forbidden to repeat words, we have to omit it. The next word that fits is MARKDOWN, we store it and continue.
#
# The next note is RE, but this time, searching a fitting word, we end doing a complete iteration over the array with finding any, so the function ends and return the definitive array solution: ["DOWN","REPTILE","AMIDST","SOFA","SOLAR","PLANE","SILENCE","MARKDOWN"]
#
# ArraysGamesAlgorithms
# Solution
def magic_music_box(words):
    if not words:
        return words
    output: list[str] = []
    order: list[str] = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
    start: int = 0
    main_valid: bool = True
    while main_valid:
        for main_idx in range(len(order)):
            valid: bool = False
            for word_idx in range(start, len(words)):
                if order[main_idx] in words[word_idx] and words[word_idx] not in output:
                    output.append(words[word_idx])
                    valid = True
                    start = word_idx + 1
                    break
            if not valid:
                for word_idx in range(len(words)):
                    if order[main_idx] in words[word_idx] and words[word_idx] not in output:
                        output.append(words[word_idx])
                        valid = True
                        start = word_idx + 1
                        break
                if not valid:
                    return output
    return output