# Write a function convert_temp(temp, from_scale, to_scale) converting temperature from one scale to another. Return converted temp value.
#
# Round converted temp value to an integer(!).
#
# Reading: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
#
# possible scale inputs:
#     "C"  for Celsius
#     "F"  for Fahrenheit
#     "K"  for Kelvin
#     "R"  for Rankine
#     "De" for Delisle
#     "N"  for Newton
#     "Re" for Réaumur
#     "Ro" for Rømer
# temp is a number, from_scale and to_scale are strings.
#
# convert_temp(   100, "C",  "F") # => 212
# convert_temp(    40, "Re", "C") # => 50
# convert_temp(    60, "De", "F") # => 140
# convert_temp(373.15, "K",  "N") # => 33
# convert_temp(   666, "K",  "K") # => 666
# FUNCTIONAL PROGRAMMINGDATA STRUCTURESSTRINGSMATHEMATICSFUNDAMENTALS
# Solution O(1) O(1)
    return temp
def convert_temp(temp, from_scale, to_scale):
    if from_scale == to_scale: return temp
    scale = {
        'C': {
            'C': lambda x: x,
            'F': lambda x: x * (9 / 5) + 32,
            'K': lambda x: x + 273.15,
            'R': lambda x: (x + 273.15) * (9 / 5),
            'De': lambda x: (100 - x) * (3 / 2),
            'N': lambda x: x * (33 / 100),
            'Re': lambda x: x * (4 / 5),
            'Ro': lambda x: (x * (21/40) + 7.5)
        },
        'F': {'C': lambda x: (x - 32) * (5 / 9)},
        'K': {'C': lambda x: x - 273.15},
        'R': {'C': lambda x: (x - 491.67) * (5 / 9)},
        'De': {'C': lambda x: 100 - x * (2 / 3)},
        'N': {'C': lambda x: x * (100 / 33)},
        'Re': {'C': lambda x: x * (5 / 4)},
        'Ro': {'C': lambda x:  (x - 7.5) * (40/21)}
    }
    celsius = scale.get(from_scale).get('C')(temp)
    return int(scale.get('C').get(to_scale)(celsius))