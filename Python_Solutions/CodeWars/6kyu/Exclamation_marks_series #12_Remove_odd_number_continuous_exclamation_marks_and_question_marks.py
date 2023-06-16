# Description:
# Remove odd number continuous exclamation marks and question marks(from the left to the right),
# until no continuous exclamation marks and question marks exist. Please note: One exclamation mark or
# question mark is not a continuous exclamation marks or question marks. The string only contains ! and ?.
#
# Examples
# remove("") === ""
# remove("!") === "!"
# remove("!!") === "!!"
# remove("!!!") === ""
# remove("!??") === "!??"
# remove("!???") === "!"
# remove("!!!??") === "??"
# remove("!!!???") === ""
# remove("!??") === "!??"
# remove("!???!!") === ""
# ("!???!!" --> "!!!" --> "")
# remove("!????!!!?") === "!"
# ("!????!!!?" --> "!?????" --> "!")
# Note
# Please don't post issue about difficulty or duplicate.
#
# FUNDAMENTALS