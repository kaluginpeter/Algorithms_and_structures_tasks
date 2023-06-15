# *************************
# *  Create a frame!      *
# *           __     __   *
# *          /  \~~~/  \  *
# *    ,----(     ..    ) *
# *   /      \__     __/  *
# *  /|         (\  |(    *
# * ^  \  /___\  /\ |     *
# *    |__|   |__|-..     *
# *************************
# Given an array of strings and a character to be used as border, output the frame with the content inside.
#
# Notes:
#
# Always keep a space between the input string and the left and right borders.
# The biggest string inside the array should always fit in the frame.
# The input array is never empty.
# Example
# frame(['Create', 'a', 'frame'], '+')
#
# Output:
#
# ++++++++++
# + Create +
# + a      +
# + frame  +
# ++++++++++
# STRINGSARRAYSASCII ARTFUNDAMENTALS
# Solution
def frame(text, char):
    text_lens = [len(i) for i in text]
    longest_len = max(text_lens)
    frame_list = [char*(longest_len + 4)]
    for i in text:
         frame_list.append("{} {}{} {}".format(char, i, " " * (longest_len - len(i)), char))
    frame_list.append(char*(longest_len + 4))
    return "\n".join(frame_list)