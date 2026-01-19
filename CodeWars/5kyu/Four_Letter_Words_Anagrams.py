# Our Setup
# Alice and Bob work in an office. When the workload is light and the boss isn't looking, they sometimes play simple word games for fun. This is one of those days!
#
# However, yesterday Carol and Dan got wise to these sneaky shenanigans ~ and so today surprise challenged them (as a team) to one of their own games, which they like to call Anagrams! Alice and Bob reluctantly agreed if all four vowed to keep their illicit gamery completely hidden from the rest of the office...
#
# Today's Game
# Team_One will be Alice & Bob versus Team_Two who are Carol & Dan, and the fun begins with a list of four-letter subject words. Going through the words on this list, the two teams compete in a game of points where one player from each team will successively take each other on one round at a time, recalling as many anagrams as possible of a subject word from their respective memories, which themselves are also lists of four-letter words.
#
# A Round
# Within each round (Alice or Bob) will be matched with (Carol or Dan) in head-on competition over a single subject word, attempting to win the round for their team by earning the most round points.
#
# Both players immediately get one (1) round point if they can simply recall the subject word itself from their memory.
#
# Player One recalls as many anagrams of the subject word as they can, getting two (2) round points for each of them.
#
# Player Two may now recall any further anagrams Player One did not know, getting three (3) round points for each.
#
# The player with the highest round score wins the round, and one (1) final point will be contributed to their team's final score. If their round scores match, they tie, and no final points are awarded for the round.
#
# The Order
# Because the first person to play in a round has the point advantage, The Order of Rounds (as shown below) was determined by having the teams take turns where one of their members gets to be first to play, and was then extended to give all players at least a chance to eventually compete against both members of their opposing team within a game:
#
# 1. Alice Vs Carol
# 2. Carol Vs Bob
# 3. Bob   Vs Dan
# 4. Dan   Vs Alice
#
# 5. Alice Vs Dan
# 6. Carol Vs Alice
# 7. Bob   Vs Carol
# 8. Dan   Vs Bob
# Because the amount of subject words will vary, each new game will begin with randomly chosen starting opponents, and from there continuously rotate through The Order of Rounds (as shown above) until all subject words have been used. The players Alice, Bob, Carol, and Dan will be represented by the integers 0, 1, 2, and 3, respectively, as exemplified in the example shown below.
#
# Your Task
# To determine a winner by figuring out which team will score the most final points!
#
# Input
# subjects
# a(n) array / list / tuple / vector of strings
# subjects will contain (1<=size<=50) words
# memories
# a(n) array / list / tuple / vector of the memories of the four players
# each memory is a(n) array / list / tuple / vector of strings
# all four players will have a memory of the same size at (1<=size<=400)
# players
# a(n) array / list / tuple / vector of a pairing of integers
# contains two (2) of the following integers representing the starting players:
#                          Team One                            Team Two
#                               0    for Alice                        2    for Carol
#                               1    for Bob                          3    for Dan
#       All strings in this kata will be valid English language  four-letter words.
#       The subjects list will not contain words that are anagrams of each other.
#       Words are from a shared source, thus some could appear in multiple lists,
#       yet the memory and subjects lists will each not contain duplicated words.
#
# Output
# An integer:
#
#   0    if Team One wins (Alice & Bob)
#   1    if Team Two wins (Carol & Dan)
# -1    if neither win because they tie
# An Example
# subjects = ('darb', 'bust', 'spot', 'calo', 'oaky', 'mite',
#             'meta', 'tael', 'gore', 'elan', 'code', 'demo')
#
# alice = ('gore', 'stop', 'emit', 'tame', 'mode',
#          'cola', 'drab', 'ergo', 'dome', 'bard',
#          'okay', 'loca', 'stub', 'goer', 'coal')
#
# bob   = ('lean', 'tela', 'stop', 'leat', 'code',
#          'pots', 'coed', 'post', 'buts', 'tale',
#          'stub', 'spot', 'tame', 'meat', 'mate')
#
# carol = ('brad', 'tame', 'okay', 'bust', 'time',
#          'lane', 'item', 'mate', 'ergo', 'darb',
#          'tubs', 'team', 'gore', 'ogre', 'meta')
#
# dan   = ('coal', 'oaky', 'tops', 'mode', 'spot',
#          'code', 'demo', 'calo', 'teal', 'opts',
#          'deco', 'cola', 'tale', 'kayo', 'late')
#
# memories = (alice, bob, carol, dan)
#
# players  = (0, 2)  #  this game begins with Alice Vs Carol
#                 Nota Bene :
#                     there are twelve possible scoring scenarios for this game,
#                     all of which have been represented once each (out of order)
#                     within the twelve rounds of this comprehensive example
#
# The game begins with Alice of Team One going first against Carol of Team Two. In this particular case, only Carol happens to know the subject word, but because their round scores match, there is no change to the final score.
# Round One ~ "darb"
#   Scenario 9 (second knows subject, players tie)
#
#        Alice    4 round points    2 each for "bard", "drab"
#
#        Carol    4 round points    1 for knowing "darb"
#                                   3 for knowing "brad"
#
#   [0, 0] teams are tied
# Following The Order of Rounds, Carol will now get to go first in taking on Bob. Bob is representing Team One which now must go in second place, but since he knows enough anagrams of the subject word, he wins the round for Team One.
# Round Two ~ "bust"
#   Scenario 5 (first knows subject, second wins)
#
#        Carol    3 round points    1 for knowing "bust"
#                                   2 for knowing "tubs"
#
#        Bob      6 round points    3 each for "buts", "stub"
#
#   [1, 0] Team One winning
# Here both players know a lot of anagrams, but they still happen to tie the round.
# Round Three ~ "spot"
#   Scenario 3 (both know subject, players tie)
#
#        Bob      7 round points    1 for knowing "spot"
#                                   2 each for "post", "pots", "stop"
#
#        Dan      7 round points    1 for knowing "spot"
#                                   3 each for "opts", "tops"
#
#   [1, 0] Team One winning
# Dan from Team Two finally gets to go first, bringing the score back to a tie by beating Alice.
# Round Four ~ "calo"
#   Scenario 4 (first knows subject, first wins)
#
#        Dan      5 round points    1 for knowing "calo"
#                                   2 each for "coal", "cola"
#
#        Alice    3 round points    3 for knowing "loca"
#
#   [1, 1] teams are tied
# A feisty Dan, this time following Alice, manages to grab a second win in a row from her, now putting Team Two in the lead.
# Round Five ~ "oaky"
#   Scenario 8 (second knows subject, second wins)
#
#        Alice   2 round points    2 for knowing "okay"
#
#        Dan     4 round points    1 for knowing "oaky"
#                                  3 for knowing "kayo"
#
#   [1, 2] Team Two winning
# Now Carol will continue the hot run of Team Two beating poor Alice yet again by just edging her out for another round.
# Round Six ~ "mite"
#   Scenario 10 (neither knows subject, first wins)
#
#        Carol    4 round points    2 each for "item", "time"
#
#        Alice    3 round points    3 for knowing "emit"
#
#   [1, 3] Team Two winning
# Bob reverses the energy by clawing out a win for Team One in this round by knowing a lot of anagrams for "meta" although without actually knowing "meta" itself.
# Round Seven ~ "meta"
#   Scenario 7 (second knows subject, first wins)
#
#        Bob      6 round points    2 each for "mate", "meat", "tame"
#
#        Carol    4 round points    1 for knowing "meta"
#                                   3 for knowing "team"
#
#   [2, 3] Team Two winning
# Both players struggle here for a victory, but the round results in a tie, with Team Two holding onto the lead.
# Round Eight ~ "tael"
#   Scenario 12 (neither knows subject, players tie)
#
#        Dan      6 round points    2 each for "late", "tale", "teal"
#
#        Bob      6 round points    3 each for "leat", "tela"
#
#   [2, 3] Team Two winning
# This time Alice finally gets some revenge against Carol, evening out the final score.
# Round Nine ~ "gore"
#   Scenario 1 (both know subject, first wins)
#
#        Alice    5 round points    1 for knowing "gore"
#                                   2 each for "ergo", "goer"
#
#        Carol    4 round points    1 for knowing "gore"
#                                   3 for knowing "ogre"
#
#   [3, 3] teams are tied
# Although neither player can muster much muck against the subject word "elan", Bob nonetheless furthers the current winning rally for Team One, and takes them back into the lead.
# Round Ten ~ "elan"
#   Scenario 11 (neither knows subject, second wins)
#
#         Carol    2 round points    2 for knowing "lane"
#
#         Bob      3 round points    3 for knowing "lean"
#
#   [4, 3] Team One winning
# In this penultimate round, Dan manages to bring some hope of victory to Team Two by leveling the score with only one subject word to go!
# Round Eleven ~ "code"
#   Scenario 2 (both know subject, second wins)
#
#         Bob      3 round points    1 for knowing "code"
#                                    2 for knowing "coed"
#
#         Dan      4 round points    1 for knowing "code"
#                                    3 for knowing "deco"
#
#   [4, 4] teams are tied
# With the final round upon us, Dan gets to go first and also knows the subject word but otherwise not enough anagrams to get any more points than Alice can. Being tied going into and also for the final round, the outcome of the game itself results in a tie.
# Round Twelve ~ "demo"
#   Scenario 6 (first knows subject, players tie)
#
#         Dan      3 round points    1 for knowing "demo"
#                                    2 for knowing "mode"
#
#         Alice    3 round points    3 for knowing "dome"
#
#   [4, 4] teams are tied
# Enjoy!
# ...and please consider one of the following kata to solve next:
#
# Shuffle an Integer
# Minimum Percentage of Visitors that Ate All Foods
# Is Sator Square?
# Playing With Toy Blocks ~ Can you build a 4x4 square?
# Four Letter Words ~ Mutations
# Crossword Puzzle! (2x2)
# Interlocking Binary Pairs
# Setting Places for the Dead
# AlgorithmsGamesGame SolversListsStringsParsingFundamentals
# Solution
def anagrams(subjects, memories, players):
    order = [
        (0, 2), (2, 1), (1, 3), (3, 0),
        (0, 3), (2, 0), (1, 2), (3, 1)
    ]
    start = order.index(tuple(players))
    score = [0, 0]
    mem_sets = []
    for mem in memories:
        d = {}
        for w in mem: d.setdefault(''.join(sorted(w)), set()).add(w)
        mem_sets.append(d)
    for i, subject in enumerate(subjects):
        p1, p2 = order[(start + i) % 8]
        team1 = 0 if p1 < 2 else 1
        team2 = 0 if p2 < 2 else 1
        sig = ''.join(sorted(subject))
        m1 = mem_sets[p1].get(sig, set())
        m2 = mem_sets[p2].get(sig, set())
        s1 = 1 if subject in m1 else 0
        s2 = 1 if subject in m2 else 0
        a1 = m1 - {subject}
        a2 = m2 - {subject}
        s1 += 2 * len(a1)
        s2 += 3 * len(a2 - a1)
        if s1 > s2: score[team1] += 1
        elif s2 > s1: score[team2] += 1
    if score[0] > score[1]: return 0
    if score[1] > score[0]: return 1
    return -1