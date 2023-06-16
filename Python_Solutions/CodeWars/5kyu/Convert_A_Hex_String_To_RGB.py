# When working with color values it can sometimes be useful to extract the individual red,
# green, and blue (RGB) component values for a color. Implement a function that meets these requirements:
#
# Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
# Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
# Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")
#
# Example
# "#FF9933" --> {r: 255, g: 153, b: 51}
# PARSINGSTRINGSALGORITHMS
# Solution
def hex_string_to_RGB(hex_string):
    colors = [int(hex_string.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)]
    return {'r':colors[0], 'g':colors[1], 'b':colors[2]}