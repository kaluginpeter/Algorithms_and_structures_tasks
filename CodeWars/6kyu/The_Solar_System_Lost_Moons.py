# Oh no! The planets are jumbled up and they have lost their moons!
#
# TASK
# Given two lists, the planets and the moons, you have to return a two-dimensional list with the planets and their respective moons.
#
# The dictionary with the planets' names (in the correct order) as the keys and their iconic moons' names as the values is given preloaded with the name planet_moons:
#
# planet_moons = {
#     'Mercury': [],
#     'Venus': [],
#     'Earth': ['Moon'],
#     'Mars': ['Deimos', 'Phobos'],
#     'Jupiter': ['Callisto', 'Europa', 'Ganymede', 'Io'],
#     'Saturn': ['Dione', 'Iapetus', 'Rhea', 'Tethys', 'Titan'],
#     'Uranus': ['Ariel', 'Miranda', 'Oberon', 'Titania', 'Umbriel'],
#     'Neptune': ['Nereid', 'Proteus', 'Triton']
# }
# The names of all the moons are sorted.
#
# Mercury and Venus have no moons at all.
#
# The moons list will have random assorted moons. The planets list will have some (or all) planets, in any order.
#
# What you return should have a list for each planet with the moons you found for it. The planets should be ordered as per the order in the planet_moons dictionary, which is ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].
#
# If a moon is present but its planet is not, ignore it
#
# The moons for each planet should be sorted and are then swept up by the planet on alternative sides. The first moon goes on the right of the planet, the next one on the left, and so on.
#
# For example, if "Saturn" is given in the planets, and the moons are ["Rhea", "Tethys", "Iapetus", "Dione"], the first moon (after sorting), "Dione", is put on the right. The next moon, "Iapetus", now goes to the left of "Saturn". "Rhea" this time has to go to the right of "Saturn". Last, "Tethys" goes to the left, because the moons have to be placed alternatively. So "Saturn"'s orbit after collecting its lost planets would look like ["Tethys", "Iapetus", "Saturn", "Dione", "Rhea"].
#
# EXAMPLE
# If the planets are ["Venus", "Neptune", "Jupiter", "Earth", "Mars"] and the moons are ["Proteus", "Rhea", "Io", "Moon", "Nereid", "Triton", "Phobos"], the Solar System you return should be:
#
# [["Venus"], ["Earth", "Moon"], ["Mars", "Phobos"], ["Jupiter", "Io"], ["Proteus", "Neptune", "Nereid", "Triton"]]
#
# # "Venus" is alone in its orbit
# # "Earth" has its (our) "Moon" given, so it's found and put to the right
# # "Mars" finds "Phobos" and puts it to the right, but "Deimos", its other moon is not given, and remains lost
# # "Jupiter" only finds "Io" from its moons
# # "Neptune" first takes "Nereid", even though "Proteus" comes first in the list of moons, "Nereid" comes first after sorting.
# # Next it puts "Proteus" to the left, and finally "Triton" again to the right.
# # "Saturn" is not present in the list of planets, and so "Rhea" remains lost
# NOTES
# The planets list won't contain anything outside of the given planets and same applies for the moons list
# All the names in both the lists will be title-cased
# The Solar System series
# Jumbled Planets
# Planet Mnemonic
# Planets on the Move
# Meteor Shower
# Lost Moons
# Lists
# Solution
from preloaded import planet_moons

def lost_moons(planets, moons):
    result = []
    ordered_planets = [p for p in planet_moons if p in planets]
    for planet in ordered_planets:
        valid_moons = sorted([m for m in moons if m in planet_moons[planet]])
        orbit = [planet]
        right = True
        for moon in valid_moons:
            if right: orbit.append(moon)
            else: orbit.insert(0, moon)
            right = not right
        result.append(orbit)
    return result