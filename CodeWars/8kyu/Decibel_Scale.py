# The following formula is called the Decibel Scale:
#
# β
# =
# 10
# log
# ⁡
# 10
# (
# I
# 1
# 0
# −
# 12
# )
# β=10log
# 10
# ​
#  (
# 10
# −12
#
# I
# ​
#  )
#
# The Decibel Scale is used to determine the loudness of a sound, measured in dB:
#
# β is the result we want, defined in dB;
# We multiply the result of the logarithmic operation by 10, otherwise it'll be called "Bel Scale";
# We provide I, the intensity of the sound wave we need to find the loudness of, which is, for the purposes of this Kata, measured in 2D space and, hence, in Watts per square meter;
# Finally, we divide the intensity by the threshold of human hearing, also measured in Watts per square meter. This is the softest possible sound a human ear can hear;
# Since the threshold of human hearing involves an extremely small, long number, we need to utilize a logarithmic operation that will provide us the result in a convenient way.
# Your task is to simply calculate the loudness of a sound wave, given its intensity as a parameter to the dBScale function.
#
# Results are automatically rounded to the nearest integer by the test cases.
#
# Algorithms