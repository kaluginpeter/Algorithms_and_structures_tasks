/*
A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?

Task
Create a poker hand that has a method to compare itself to another poker hand:

Result compare (const PokerHand &player, const PokerHand &opponent);
A poker hand has a constructor that accepts a string containing 5 cards:

PokerHand hand ("KS 2H 5C JD TD");
The characteristics of the string of cards are:

Each card consists of two characters, where
The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
A space is used as card separator between cards
The result of your poker hand compare can be one of these 3 options:

enum class Result { Win, Loss, Tie };
Notes
Apply the Texas Hold'em rules for ranking the cards.
Low aces are valid in this kata.
There is no ranking for the suits.
If you finished this kata, you might want to continue with Sortable Poker Hands

GamesAlgorithmsObject-oriented Programming
*/
// Solution
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

enum class Result { Win, Loss, Tie };

struct PokerHand {
    std::vector<int> values;
    std::vector<char> suits;
    PokerHand(const char* pokerhand) {
        std::stringstream ss(pokerhand);
        std::string card;
        while (ss >> card) {
            values.push_back(value_from_char(card[0]));
            suits.push_back(card[1]);
        }
        std::sort(values.begin(), values.end(), std::greater<int>());
    }

    static int value_from_char(char c) {
        if (c >= '2' && c <= '9') return c - '0';
        if (c == 'T') return 10;
        if (c == 'J') return 11;
        if (c == 'Q') return 12;
        if (c == 'K') return 13;
        if (c == 'A') return 14;
        return 0;
    }

    std::vector<int> rank() const {
        std::vector<int> v = values;
        std::map<int,int> count;
        for (int x : v) count[x]++;
        bool flush = std::all_of(suits.begin(), suits.end(),
            [&](char s){ return s == suits[0]; });
        bool straight = false;
        int high_straight = v[0];
        if (v[0] - v[4] == 4 &&
            std::adjacent_find(v.begin(), v.end(),
                [](int a,int b){ return a - b != 1; }) == v.end()) {
            straight = true;
        }
        if (v == std::vector<int>{14,5,4,3,2}) {
            straight = true;
            high_straight = 5;
        }
        std::vector<std::pair<int,int>> groups;
        for (auto [val, cnt] : count) groups.push_back({cnt, val});
        std::sort(groups.begin(), groups.end(),
            [](auto &a, auto &b) {
                if (a.first != b.first) return a.first > b.first;
                return a.second > b.second;
            });
        if (straight && flush) return {8, high_straight};
        if (groups[0].first == 4) return {7, groups[0].second, groups[1].second};
        if (groups[0].first == 3 && groups[1].first == 2) return {6, groups[0].second, groups[1].second};
        if (flush) return {5, v[0], v[1], v[2], v[3], v[4]};
        if (straight) return {4, high_straight};
        if (groups[0].first == 3) {
            std::vector<int> res = {3, groups[0].second};
            for (int i = 1; i < groups.size(); ++i) res.push_back(groups[i].second);
            return res;
        }
        if (groups[0].first == 2 && groups[1].first == 2) return {2, groups[0].second, groups[1].second, groups[2].second};
        if (groups[0].first == 2) {
            std::vector<int> res = {1, groups[0].second};
            for (int i = 1; i < groups.size(); ++i) res.push_back(groups[i].second);
            return res;
        }
        return {0, v[0], v[1], v[2], v[3], v[4]};
    }
};

Result compare (const PokerHand &player, const PokerHand &opponent) {
    auto r1 = player.rank();
    auto r2 = opponent.rank();
    if (r1 > r2) return Result::Win;
    if (r1 < r2) return Result::Loss;
    return Result::Tie;
}