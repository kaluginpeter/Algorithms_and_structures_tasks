# Karan's company makes software that provides different features based on the version of operating system of the user.
#
# For finding which version is more recent, Karan uses the following method:
#
# While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the
# Operating system company just released OS version 10.10.
#
# Karan's function fails for the new version:
#
# compare_versions ("10.9", "10.10");       # returns True, while it should return False
# Karan now wants to spend some time to write a more robust version comparison function that works
# for any future version/sub-version updates.
#
# Help Karan write this function. Here are a few sample cases:
#
# compare_versions("11", "10");                    # returns True
# compare_versions("11", "11");                    # returns True
# compare_versions("10.4.6", "10.4");              # returns True
# compare_versions("10.4", "11");                  # returns False
# compare_versions("10.4", "10.10");               # returns False
# compare_versions("10.4.9", "10.5");              # returns False
# It can be assumed that version strings are non empty and only contain numeric literals and the character '.'.
#
# STRINGSFUNDAMENTALS
# Solution
def compare_versions(ver1, ver2):
    return [int(i) for i in ver1.split(".")] >= [int(j) for j in ver2.split(".")]