# We all love the future president (or Führer or duce or sōtō as he could find them more fitting) donald trump, but we might fear that some of his many fans like John Miller or John Barron are not making him justice, sounding too much like their (and our as well, of course!) hero and thus risking to compromise him.
#
# For this reason we need to create a function to detect the original and unique rhythm of our beloved leader, typically having a lot of extra vowels, all ready to fight the establishment.
#
# The index is calculated based on how many vowels are repeated (case-insensitively) more than once in a row and dividing them by the total number of vowels a petty enemy of America would use.
#
# For example:
#
# "I will build a huge wall" --> 0
# --> definitely not our trump: 0 on the trump score
#
# "HUUUUUGEEEE WAAAAAALL" --> 4
# --> 4 extra "U", 3 extra "E" and 5 extra "A" on 3 different vowels
# --> groups: 12/3 make for a trumpy trumping score of 4: not bad at all!
#
# "listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT" --> 1.56
# --> 14 extra vowels on 9 base ones give 1.55555555... which is rounded to 1.56
# Notes: vowels are only the ones in the patriotic group of "aeiou": "y" should go back to Greece if she thinks she can have the same rights of true American vowels; there is always going to be at least a vowel, as silence is the option of coward Kenyan/terrorist presidents and their friends.
#
# Round each result by two decimal digits: there is no place for small fry in Trump's America.
#
# Special thanks for Izabela for support and proof-reading.
#
# Regular ExpressionsStringsAlgorithms
# Solution
def trump_detector(trump_speech):
    trump_speech = trump_speech.lower()
    overall: int = 0
    in_row: int = 0
    seen: bool = False
    for i in range(len(trump_speech)):
        if trump_speech[i] in 'aeoiu':
            if i and trump_speech[i] == trump_speech[i - 1]: in_row += 1
            if not seen or (i and trump_speech[i] != trump_speech[i - 1]):
                seen = True
                overall += 1
        else: seen = False
    return round(in_row / overall, 2)