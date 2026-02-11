

# A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?
#
# Task
# Create a poker hand that has a method to compare itself to another poker hand:
#
# compare_with(self, other_hand)
# A poker hand has a constructor that accepts a string containing 5 cards:
#
# PokerHand("KS 2H 5C JD TD")
# The characteristics of the string of cards are:
#
# Each card consists of two characters, where
# The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
# The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
# A space is used as card separator between cards
# The result of your poker hand compare can be one of these 3 options:
#
# [ "Win", "Tie", "Loss" ]
# Notes
# Apply the Texas Hold'em rules for ranking the cards.
# Low aces are valid in this kata.
# There is no ranking for the suits.
# If you finished this kata, you might want to continue with Sortable Poker Hands
#
# GamesAlgorithmsObject-oriented Programming
# Solution
from collections import Counter
class PokerHand:
    RESULT = ["Loss", "Tie", "Win"]
    VALUE_MAP = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9,
        'T': 10, 'J': 11, 'Q': 12,
        'K': 13, 'A': 14
    }

    def __init__(self, hand):
        cards = hand.split()
        self.values = sorted([self.VALUE_MAP[c[0]] for c in cards],reverse=True)
        self.suits = [c[1] for c in cards]

    def rank(self):
        values = self.values[:]
        suits = self.suits
        count = Counter(values)
        flush = len(set(suits)) == 1
        straight = False
        high_straight = values[0]
        if values == list(range(values[0], values[0] - 5, -1)): straight = True
        if values == [14, 5, 4, 3, 2]:
            straight = True
            high_straight = 5
        groups = sorted([(cnt, val) for val, cnt in count.items()],reverse=True)
        if straight and flush: return [8, high_straight]
        if groups[0][0] == 4: return [7, groups[0][1], groups[1][1]]

        if groups[0][0] == 3 and groups[1][0] == 2: return [6, groups[0][1], groups[1][1]]
        if flush: return [5] + values
        if straight: return [4, high_straight]
        if groups[0][0] == 3:
            return [3, groups[0][1]] + sorted([v for v in values if v != groups[0][1]], reverse=True)
        if groups[0][0] == 2 and groups[1][0] == 2:
            pair_vals = sorted([groups[0][1], groups[1][1]], reverse=True)
            kicker = [v for v in values if v not in pair_vals][0]
            return [2] + pair_vals + [kicker]
        if groups[0][0] == 2:
            pair_val = groups[0][1]
            kickers = sorted([v for v in values if v != pair_val], reverse=True)
            return [1, pair_val] + kickers
        return [0] + values

    def compare_with(self, other):
        r1 = self.rank()
        r2 = other.rank()
        if r1 > r2: return "Win"
        elif r1 < r2: return "Loss"
        else: return "Tie"