# The characters of Chima need your help. Their weapons got mixed up! They need you to write a program that accepts the name of a character in Chima then tells which weapon he/she owns.
#
# For example: for the character "Laval" your program should return the solution "Laval-Shado Valious"
#
# You must complete the following character-weapon pairs:
#
# Laval-Shado Valious,
# Cragger-Vengdualize,
# Lagravis-Blazeprowlor,
# Crominus-Grandorius,
# Tormak-Tygafyre,
# LiElla-Roarburn.
# Return "Not a character" for invalid inputs.
#
# Fundamentals
# Solution
def identify_weapon(n):
    match n:
        case 'Laval': return 'Laval-Shado Valious'
        case 'Cragger': return 'Cragger-Vengdualize'
        case 'Lagravis': return 'Lagravis-Blazeprowlor'
        case 'Crominus': return 'Crominus-Grandorius'
        case 'Tormak': return 'Tormak-Tygafyre'
        case 'LiElla': return 'LiElla-Roarburn'
        case _: return 'Not a character'