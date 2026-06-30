# The following table describes the different types of IEEE 754 numbers.
#
# It is valid for both single-precision (SP, 32 bits) and double-precision (DP, 64 bits).
#
# Type	Sign	Exponent	Mantissa
# Infinity	Any	All 1s	All 0s
# Quiet NaN	Any	All 1s	Starts with a 1
# Signaling NaN	Any	All 1s	Starts with a 0 and contains at least one 1
# Zero	Any	All 0s	All 0s
# Denormalized numbers	Any	All 0s	At least one 1
# Normalized numbers	Any	At least one 1 and one 0	Any
# Note about NaN
# A NaN (Not a Number) is a special value that indicates an asbence of a valid number, or an erroneous operation, such as division by 0. There are 2 types of NaNs: a signalling NaN is supposed to trigger a runtime error, while a quiet NaN does not by itself result in a a program error. NaNs have the unique property of not being equal to themselves: NaN != NaN.
#
# Task
# An enumerated type representing all these possibilities has been preloaded/pre-written for you. You must write a function that takes an IEEE-754 64-bit DP float/double in parameter and returns its type.
#
# In Java it is a preloaded enum named FloatTypeEnum
# In C it is a pre-written enum named FloatType
# In JavaScript, which does not have native support for enums, it is a preloaded immutable Object named FloatType whose keys are from the list below and values are identical to the keys.
# In Python, it is a preloaded Enum from the enum standard Python module.
# In Lua, which does not have native support for enums, it is a preloaded table whose keys are from the list below and values are identical to the keys.
# In Haskell, it is a type named FloatType in the Preloaded module.
# The enumeration contains the following members:
#
# POSITIVE_DENORMALIZED
# NEGATIVE_DENORMALIZED
# POSITIVE_NORMALIZED
# NEGATIVE_NORMALIZED
# POSITIVE_INFINITY
# NEGATIVE_INFINITY
# POSITIVE_ZERO
# NEGATIVE_ZERO
# POSITIVE_QUIET_NAN
# NEGATIVE_QUIET_NAN
# POSITIVE_SIGNALING_NAN
# NEGATIVE_SIGNALING_NAN
# Notes
# You may want to solve this kata first :
#
# IEEE 754 floating point numbers
# BinaryFundamentals