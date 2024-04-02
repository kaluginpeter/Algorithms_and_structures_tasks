# Christmas Present Calculator
# After we find out if Santa can save Christmas there is another task to face.
#
# Santa's little helper aren't sick anymore. They are ready to give away presents again. But some of them are still weak.
# This leads to more productive elves than others.
#
# How many presents can Santa distribute this christmas?
#
# Your Task:
# You will get two inputs.
# One dictionary with the producitivity of each elf like the following:
#
# {"Santa": 1, "elf_1": 1, "elf_2": 1, "elf_3": 2, "elf_4": 3}
#
# and a string array with the time needed for each present like the following:
#
# "hh:mm:ss"
#
# The productivity describes the workload an elf can do each day:
#
# //productivity 1 = 24 hours each day
# //productivity 2 = 48 hours each day
# ...
#
# Return the number of present they can distribute at maximum.
#
# Note that:
#
# They have only 24 hours
# They try to give out as much as presents as possible (the ones with less time first)
# All the elves can work on multiple tasks. You can count it as one work capacity
#
#
# This kata is part of the Collection "Date fundamentals":
# #1 Count the Days!
# #2 Minutes to Midnight
# #3 Can Santa save Christmas?
# #4 How Many Presents?
# DATE TIMEFUNDAMENTALS
# Solution
from datetime import timedelta as td


def convert(arr: list[str]) -> list[int]:
    ans: list[int] = list()
    for time in arr:
        hours, minutes, seconds = map(int, time.split(':'))
        if hours >= 24:
            total_seconds: int = int(hours * 3600 + minutes * 60 + seconds)
        else:
            total_seconds: int = int(td(hours=hours, minutes=minutes, seconds=seconds).total_seconds())
        ans.append(total_seconds)
    return ans


def count_presents(prod: dict, pres: list[str]) -> int:
    times: list[int] = sorted(convert(pres))
    count: int = 0
    powers: int = sum(time * 24 * 3600 for time in prod.values())
    for gift in times:
        if powers >= gift:
            count += 1
            powers -= gift
        else:
            break
    return count