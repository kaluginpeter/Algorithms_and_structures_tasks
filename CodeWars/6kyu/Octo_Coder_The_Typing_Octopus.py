# Everybody knows what an octopus is. You've probably seen videos where they use their tentacles to manipulate objects. Opening jars, picking sticks... You name it, they can toy with it.
#
# But have you ever seen an octopus doing paperwork? Well, you probably never will, but at least you can simulate the idea.
#
# Your task is to simulate an octopus typing in a keyboard. The octopus receives the files by email and reads them in the office, but your job is only to process the text content inside those files via a given String.
#
# It can receive an email with an empty file (filled only with spaces), which means that it doesn't type.
#
# An octopus has eight tentacles, so it can type up to eight letters at once.
#
# Each round consists of the octopus typing as many letters as it can, up to eight.
#
# Sounds efficient, right? Well, there's a reason why companies don't hire octopuses. Due to their suction cups, the tentacles get stuck on the keys they press, not letting them type that letter, space or symbol again until the next round. Upper case letters will count as their lower case counterpart, not being able to write "Aa". However, thanks to the number pad numbers will be able to be typed two times each round.
#
# The missing letters will be represented with '*'.
#
# Examples:
# "Letter" -> "Let**r"
#
# "Unconcerned" -> "Unco**erned"
#
# "Can a can contain fish?" -> "Can ****n co*tain fish?"
#
# "Write 122 pages" -> "Write 122 pages"
#
# "8000 dollars went missing" -> "800* dollars went mis**ng"
#
# "             " -> "" (counts as empty file)
# Games
# Solution
def octopus(idea: str | None) -> str:
    if not idea or idea.count(' ') == len(idea): return ''
    output: list[str] = []
    for i in range(0, len(idea), 8):
        seen: dict[str, int] = dict()
        part: list[str] = []
        for j in range(i, min(i + 8, len(idea))):
            if idea[j].isdigit():
                if seen.get(idea[j], 0) == 2: part.append('*')
                else:
                    seen[idea[j]] = seen.get(idea[j], 0) + 1
                    part.append(idea[j])
            else:
                if idea[j].lower() in seen: part.append('*')
                else:
                    part.append(idea[j])
                    seen[idea[j].lower()] = 1
        output.append(''.join(part))
    return ''.join(output)