# Description
# You are a light God, living in Aladdin's lamp. If someone is rubbing the surface of the lamp, you will come out and realize his three wishes. You have an endless life, the meaning of your life is to wait for the owner to appear...
#
# One day, a traveler appeared, with a big parcel. There are some Gold coins, silver coins, waters, foods, books, weapons, clothes, medicines, tools in his big parcel, Arranged neatly, all the same items are adjacent to each other.
#
# ["gold coin","gold coin","gold coin","silver coin","silver coin",
# "water","water","water","water", "food", "food", "food", "food",
# "book","book", "weapon","weapon", "clothe","clothe", "medicine",
# "medicine", "tool", "tool"]
# He found Aladdin's lamp and hear your voice: "friction lamp, put me out, I will realize your three wishes." He wiped the dust off the lamp, a smoke burst out, and you came out from the light. The next thing is that you help him to achieve the three wishes:
#
# wish1="I want 1 food"
# wish2="I want 2 books"
# wish3="I want 1 girl"
# You will keep your promise, do your best to help him achieve his wish. Add all the things he needs to the back of the same kind. If he asks for something that does not appear in the list, add it to the end of the list.
#
# ["gold coin","gold coin","gold coin","silver coin","silver coin",
# "water","water","water","water", "food","food", "food", "food",
# "food", "book","book","book","book", "weapon","weapon", "clothe",
# "clothe", "medicine","medicine", "tool", "tool","girl"]
# If he is a greedy man, put forward such a wish: "I want n wishes"(n is a number), you will punish him, let him lose all his things, return [].
#
# Task
# Complete function threeWishes that accepts 4 arguments parcel, wish1, wish2 and wish3. Returns the result in accordance with the rules above.
#
# Note the different of singular and plural. In order to simple, we always add s to the end of the plural, the singular is not.
#
# Puzzles