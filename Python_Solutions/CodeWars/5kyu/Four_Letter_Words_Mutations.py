# Our Setup
# Alice and Bob work in an office. When the workload is light and the boss isn't looking, they play simple word games for fun. This is one of those days!
#
# Today's Game
# Alice and Bob are playing what they like to call Mutations, where they take turns trying to "think up" a new four-letter word (made up of four unique letters) that is identical to the prior word except for only one letter. They just keep on going until their memories fail out.
#
# Their Words
# Alice and Bob have memories of the same size, each able to recall 10 to 2000 different four-letter words. Memory words and initial game word are randomly taken from the same list of 4000 (unique, four-letter, lowercased) words, any of which may appear in both memories.
#
# The expression to "think up" a new word means that for their turn, the player must submit as their response word the first valid, unused word that appears in their memory (by lowest array index), as their memories are ordered from the most "memorable" words to the least.
#
# The Rules
# a valid response word must contain four unique letters
# 1 letter is replaced while the other 3 stay in position
# it must be the lowest indexed valid word in that memory
# this word cannot have already been used during the game
# the final player to provide a valid word will win the game
# if 1st player fails 1st turn, 2nd can win with one word
# when both players fail the initial word, there is no winner
# Your Task
# To determine the winner!
#
# Some Examples
# alice = plat,rend,bear,soar,mare,pare,flap,neat,clan,pore
#
# bob   = boar,clap,farm,lend,near,peat,pure,more,plan,soap
#
# In the case of word = "send" and first = 0:
# Alice responds to send with rend
# Bob responds to rend with lend
# Alice has no valid response to lend
# Bob wins the game.
# In the case of word = "flip" and first = 1:
# Bob has no valid response to flip
# Alice responds to flip with flap
# Alice wins the game.
# In the case of word = "calm" and first = 1:
# Bob has no valid response to calm
# Alice has no valid response to calm
# Neither wins the game.
# In the case of word = "more" and first = 1:
# Bob has no valid response to more **
# Alice responds to more with mare
# Alice wins the game.
# In the case of word = "maze" and first = 0:
# Alice responds to maze with mare
# Bob responds to mare with more **
# Alice responds to more with pore
# Bob responds to pore with pure
# Alice responds to pure with pare
# Bob has no valid response to pare
# Alice wins the game.
# ** Note that in these last two cases, Bob cannot use mere because it has two e's.
#
# Input
# alice  #  list of words in Alice's memory (10 <= n <= 2000)
# bob    #  list of words in Bob's memory (same size as alice)
# word   #  string of the initial challenge word of the game
# first  #  integer of whom begins: 0 for Alice, 1 for Bob
# Output
# return  0  #  if Alice wins
# return  1  #  if Bob wins
# return -1  #  if both fail
# Enjoy!
# You may consider one of the following kata to solve next:
#
# Playing With Toy Blocks ~ Can you build a 4x4 square?
# Crossword Puzzle! (2x2)
# Interlocking Binary Pairs
# Is Sator Square?
# STRINGSARRAYSGAMESPARSINGALGORITHMS
def delete_unsupported(arr: list[str], target: str) -> None:
    for i in range(len(arr) - 1, -1, -1):
        if len(set(arr[i])) != 4 or arr[i] == target: arr.pop(i)


def find_word(words: list[str], target: str) -> tuple[bool, str]:
    word: str = ''
    for i in range(len(words)):
        if sum(x != y for x, y in zip(words[i], target)) <= 1:
            word = words[i]
            words.pop(i)
            return True, word
    return False, word


def mutations(alice, bob, word, first):
    alice_, bob_ = alice[::], bob[::]
    delete_unsupported(alice_, word)
    delete_unsupported(bob_, word)
    users: dict[int, str] = {0: 'Alice', 1: 'Bob'}
    user_words: dict[str, list[str]] = {'Alice': alice_, 'Bob': bob_}
    user: int = first
    idx: int = 0
    stack: list[tuple[int, bool]] = list()
    prev_winner: int = 0
    while True:
        step = find_word(user_words.get(users[user]), word)
        stack.append((user, step[0]))
        if step[0]:
            prev_winner = user
            delete_unsupported(alice_, step[1])
            delete_unsupported(bob_, step[1])
        word = step[1] if step[0] else word
        user = int(not bool(user))

        step = find_word(user_words.get(users[user]), word)
        stack.append((user, step[0]))
        if step[0]:
            prev_winner = user
            delete_unsupported(alice_, step[1])
            delete_unsupported(bob_, step[1])

        word = step[1] if step[0] else word

        if stack[0][1] == stack[1][1] == False and idx == 0:
            return -1
        elif stack[0][1] == stack[1][1] == False:
            return prev_winner
        elif stack[0][1] == True and stack[1][1] == False:
            return stack[0][0]
        elif stack[0][1] == False and stack[1][1] == True:
            return stack[1][0]
        user = int(not bool(user))
        stack = []
        idx += 1
    return -1