# Are you a file extension master? Let's find out by checking if Bill's files are
# images or audio files. Please use regex if available natively for your language.
#
# You will create 2 string methods:
#
# isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible),
# with the extension .mp3, .flac, .alac, or .aac.
#
# isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible),
# with the extension .jpg, .jpeg, .png, .bmp, or .gif.
#
# Note that this is not a generic image/audio files checker. It's meant to be a test for
# Bill's files only. Bill doesn't like punctuation. He doesn't like numbers, neither.
# Thus, his filenames are letter-only
#
# Rules
#
# It should return true or false, simply.
# File extensions should consist of lowercase letters and numbers only.
# File names should consist of letters only (uppercase, lowercase, or both)
# Good luck!
#
# STRINGSREGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def is_audio(file_name):
    return any(file_name.endswith(i) for i in ['.mp3', '.flac', '.alac', '.aac']) and all(i.isalpha() for i in file_name.split('.')[0])
def is_img(file_name):
    return any(file_name.endswith(i) for i in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']) and all(i.isalpha() for i in file_name.split('.')[0])