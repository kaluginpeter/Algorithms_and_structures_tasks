# No Story
#
# No Description
#
# Only by Thinking and Testing
#
# Look at result of testcase, guess the code!
#
# Series
# 01:A and B?
# 02:Incomplete string
# 03:True or False
# 04:Something capitalized
# 05:Uniq or not Uniq
# 06:Spatiotemporal index
# 07:Math of Primary School
# 08:Math of Middle school
# 09:From nothingness To nothingness
# 10:Not perfect? Throw away!
# 11:Welcome to take the bus
# 12:A happy day will come
# 13:Sum of 15(Hetu Luosliu)
# 14:Nebula or Vortex
# 15:Sport Star
# 16:Falsetto Rap Concert
# 17:Wind whispers
# 18:Mobile phone simulator
# 19:Join but not join
# 20:I hate big and small
# 21:I want to become diabetic ;-)
# 22:How many blocks?
# 23:Operator hidden in a string
# 24:Substring Magic
# 25:Report about something
# 26:Retention and discard I
# 27:Retention and discard II
# 28:How many "word"?
# 29:Hail and Waterfall
# 30:Love Forever
# 31:Digital swimming pool
# 32:Archery contest
# 33:The repair of parchment
# 34:Who are you?
# 35:Safe position
# Special recommendation
# Another series, innovative and interesting, medium difficulty. People who like to challenge, can try these kata:
#
# Play Tetris : Shape anastomosis
# Play FlappyBird : Advance Bravely
# Puzzles
# Solution
def testit(s):
    if len(s) < 2: return s
    output: list[str] = []
    for i in range(0, len(s), 2):
        if i + 1 == len(s):
            output.append(s[i])
            continue
        output.append(chr(((ord(s[i]) - 96) + (ord(s[i + 1]) - 96)) // 2 + 96))
    return ''.join(output)