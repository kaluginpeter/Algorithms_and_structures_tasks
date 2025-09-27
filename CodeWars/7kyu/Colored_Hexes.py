# You're looking through different hex codes, and having trouble telling the difference between #000001 and #100000
#
# We need a way to tell which is red, and which is blue!
#
# That's where you create hex color !!!
#
# It should read an RGB input, and return whichever value (red, blue, or green) is of greatest concentration!
#
# But, if multiple colors are of equal concentration, you should return their mix!
#
# red + blue = magenta
#
# green + red = yellow
#
# blue + green = cyan
#
# red + blue + green = white
# One last thing, if the string given is empty, or has all 0's, return black!
#
# Examples:
#
# codes = "087 255 054" -> "green"
# codes = "181 181 170" -> "yellow"
# codes = "000 000 000" -> "black"
# codes = "001 001 001" -> "white"
# Fundamentals
# Solution
def hex_color(codes: str) -> str:
    if not codes:
        return "black"
    parts = codes.split()
    if len(parts) != 3:
        return "black"

    r, g, b = map(int, parts)
    if r == g == b == 0:
        return "black"
    m = max(r, g, b)
    channels = []
    if r == m:
        channels.append("red")
    if g == m:
        channels.append("green")
    if b == m:
        channels.append("blue")
    if len(channels) == 1:
        return channels[0]
    if len(channels) == 2:
        if "red" in channels and "blue" in channels:
            return "magenta"
        if "red" in channels and "green" in channels:
            return "yellow"
        if "blue" in channels and "green" in channels:
            return "cyan"
    return "white"