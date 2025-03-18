# In western countries 13 is an unlucky number. Many hotels have no floor 13, and no room number 13. In China, more numbers are considered unlucky: 18 is an unlucky floor, because Chinese believe that hell has eighteen floors underground. 4 is a unlucky number too, because in Chinese, four has the same pronunciation as death.
#
# So, a Chinese hotel has no floor numbers including 4, 13 or 18, such as 24, 40, 104, 113, 130, ... and no room numbers including 4 or 13 (but 18 can appear).
#
# Task
# Suppose you work in a Chinese hotel, and you are given the real floor number and the total number of rooms on the floor; you need to give all the room numbers in ascending order that do not contain any unlucky numbers.
#
# Complete the function that accepts 2 arguments: realFloor and totalRooms. Return the result in accordance with the rules above.
#
# Notes:
#
# use 2 digits for the room numbers, but when the largest room number is above 99, use 3 digits
# if 1 comes from floor number, but 3 comes from room number, then 1 and 3 will not be considered as 13 (imagine this is because the floor number and room number have different colors, or some other reasons ;-)
# 0 < realFloor < 150
# 0 < totalRooms < 150
# Examples
# floor:  1
# rooms: 10
# The result should be:
# [ "101", "102", "103", "105", "106", "107", "108", "109", "110", "111" ]
# // room 104 is skipped
# floor:  4
# rooms: 30
# The result should be:
# [ "501", "502", "503", "505", "506", "507", "508", "509", "510", "511",
#   "512", "515", "516", "517", "518", "519", "520", "521", "522", "523",
#   "525", "526", "527", "528", "529", "530", "531", "532", "533", "535" ]
# // floor 4 is skipped
# // rooms 504, 513, 514, 524, 534 are skipped
# floor: 100
# rooms: 100
# The result should be:
# [ "126001", "126002", "126003", "126005", "126006", "126007", "126008",
#   ...
#   "126118", "126119", "126120", "126121", "126122", "126123", "126125" ]
# // floors 4, 13, 14, 18, 24, 34, 40-49, 54, 64, 74, 84, 94, 104, 113, 114, 118, 124 are skipped
# // rooms 4, 13, 14, 24, 34, 40-49, 54, 64, 74, 84, 94, 104, 113, 114, 124 are skipped
# Puzzles