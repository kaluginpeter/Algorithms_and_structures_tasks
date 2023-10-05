# Were you ever interested in the phenomena of astrology, star signs, tarot, voodoo ? (ok not voodoo that's too spooky)...
# Task:
# Your job for today is to finish the star_sign function by finding the astrological sign, given the birth details as a Date object.
# Start and end dates for zodiac signs vary on different resources so we will use this table to get consistent results:
#
# Aquarius ------ 21 January - 19 February
# Pisces --------- 20 February - 20 March
# Aries ---------- 21 March - 20 April
# Taurus -------- 21 April - 21 May
# Gemini -------- 22 May - 21 June
# Cancer -------- 22 June - 22 July
# Leo ------------- 23 July - 23 August
# Virgo ----------- 24 August - 23 September
# Libra ----------- 24 September - 23 October
# Scorpio -------- 24 October - 22 November
# Sagittarius ---- 23 November - 21 December
# Capricorn ----- 22 December - 20 January
#
# Test info: 100 random tests (dates range from January 1st 1940 until now)
# DATE TIMEPUZZLES
# Solution
def star_sign(date):
    m, d = date.month, date.day
    signs = [(1,20,"Capricorn"), (2,19,"Aquarius"), (3,20,"Pisces"), (4,20,"Aries"),
            (5,21,"Taurus"), (6,21,"Gemini"), (7,22,"Cancer"), (8,23,"Leo"),
            (9,23,"Virgo"), (10,23,"Libra"), (11,22,"Scorpio"), (12,21,"Sagittarius"),
            (12,31,"Capricorn")]
    for i in range(len(signs)):
        if signs[i][0] == m:
            if d <= signs[i][1]:
                return signs[i][2]
            return signs[i + 1][2]