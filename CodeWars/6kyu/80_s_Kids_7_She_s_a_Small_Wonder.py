# Vicky is quite the small wonder. Most people don't even realize she's not a real girl, but a robot living amongst us. Sure, if you stick around her home for a while you might see her creator open up her back and make a few tweaks and even see her recharge in the closet instead of sleeping in a bed.
#
# In this kata, we're going to help Vicky keep track of the words she's learning.
#
# Write a function, learnWord(word) ( LearnWord(word) in C# ) which is a method of the Robot object. The function should report back whether the word is now stored, or if she already knew the word.
#
# Example:
#
# var vicky = new Robot();
# vicky.learnWord('hello') -> 'Thank you for teaching me hello'
# vicky.learnWord('abc') -> 'Thank you for teaching me abc'
# vicky.learnWord('hello') -> 'I already know the word hello'
# vicky.learnWord('wow!') -> 'I do not understand the input'
# Case shouldn't matter. Only alpha characters are valid. There's also a little trick here. Enjoy!
#
# Check out my other 80's Kids Katas:
# 80's Kids #1: How Many Licks Does It Take
# 80's Kids #2: Help Alf Find His Spaceship
#
# 80's Kids #3: Punky Brewster's Socks
#
# 80's Kids #4: Legends of the Hidden Temple
#
# 80's Kids #5: You Can't Do That on Television
#
# 80's Kids #6: Rock 'Em, Sock 'Em Robots
#
# 80's Kids #7: She's a Small Wonder
#
# 80's Kids #8: The Secret World of Alex Mack
#
# 80's Kids #9: Down in Fraggle Rock
#
# 80's Kids #10: Captain Planet
#
# FundamentalsObject-oriented Programming
# Solution
class Robot:
    def __init__(self) -> None:
        self.dataset: set[str] = set()
        for word in 'thank you for teaching me'.split(): self.dataset.add(word)
        for word in 'i already know the word'.split(): self.dataset.add(word)
        for word in 'i do not understand the input'.split(): self.dataset.add(word)

    def learn_word(self, word: str) -> str:
        if not word or any(not char.isalpha() for char in word):
            return 'I do not understand the input'
        elif word.lower() in self.dataset:
            return f'I already know the word {word}'
        self.dataset.add(word.lower())
        return f'Thank you for teaching me {word}'