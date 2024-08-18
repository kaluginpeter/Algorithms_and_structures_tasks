# Introduction
# In the United Kingdom, the driving licence is the official document which authorises its holder to operate various types of motor vehicle on highways and some other roads to which the public have access. In England, Scotland and Wales they are administered by the Driver and Vehicle Licensing Agency (DVLA) and in Northern Ireland by the Driver & Vehicle Agency (DVA). A driving licence is required in the UK by any person driving a vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective of ownership of the land over which the road passes, thus including many which allow the public to pass over private land; similar requirements apply in Northern Ireland under the Road Traffic (Northern Ireland) Order 1981. (Source Wikipedia)
# Driving
# Task
# The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information
# Rules
# 1–5: The first five characters of the surname (padded with 9s if less than 5 characters)
#
# 6: The decade digit from the year of birth (e.g. for 1987 it would be 8)
#
# 7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)
#
# 9–10: The date within the month of birth
#
# 11: The year digit from the year of birth (e.g. for 1987 it would be 7)
#
# 12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name
#
# 14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9
#
# 15–16: Two computer check digits. We will always use "AA"
# Your task is to code a UK driving license number using an Array of data. The Array will look like
#
# data = ["John","James","Smith","01-Jan-2000","M"]
# Where the elements are as follows
#
# 0 = Forename
# 1 = Middle Name (if any)
# 2 = Surname
# 3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
# 4 = M-Male or F-Female
# You will need to output the full 16 digit driving license number.
#
# Good luck and enjoy!
#
# Kata Series
# If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.
#
# Rank
# Maze Runner
#
# Rank
# Scooby Doo Puzzle
#
# Rank
# Driving License
#
# Rank
# Connect 4
#
# Rank
# Vending Machine
#
# Rank
# Snakes and Ladders
#
# Rank
# Mastermind
#
# Rank
# Guess Who?
#
# Rank
# Am I safe to drive?
#
# Rank
# Mexican Wave
#
# Rank
# Pigs in a Pen
#
# Rank
# Hungry Hippos
#
# Rank
# Plenty of Fish in the Pond
#
# Rank
# Fruit Machine
#
# Rank
# Car Park Escape
#
# STRINGSARRAYSFUNDAMENTALS
# Solution
from dateutil.parser import parse
def driver(data):
    lic = ""
    if len(data[2]) >= 5:
          lic += data[2][:5]
    else:
            lic += data[2]
            while (len(lic) < 5): lic += "9"
    lic += (str(parse(data[3]).year))[2]
    month = parse(data[3]).month
    if data[4] == "F": month += 50
    month = str(month)
    if len(month) == 1: month = "0" + month
    lic += month
    day = str(parse(data[3]).day)
    if len(day) == 1: day = "0" + day
    lic += day
    lic += (str(parse(data[3]).year))[3]
    lic +=  data[0][:1]
    if (data[1]) != "":
        lic += data[1][:1]
    else:
        lic += "9"
    lic += "9AA"
    return lic.upper()