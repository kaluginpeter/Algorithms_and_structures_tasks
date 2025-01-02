# You are the judge at a competitive eating competition and you need to choose a winner!
#
# There are three foods at the competition and each type of food is worth a different amount of points. Points are as follows:
#
# Chickenwings: 5 points
#
# Hamburgers: 3 points
#
# Hotdogs: 2 points
#
# Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the participants, for example:
#
# [
#   {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
#   {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
# ]
# It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.
#
# [
#   {name: "Big Bob", score: 134},
#   {name: "Habanero Hillary", score: 98}
# ]
# Happy judging!
#
# Object-oriented ProgrammingFundamentals
# Solution
def scoreboard(who_ate_what):
    return [{
            'name': item['name'],
            'score': item.get('chickenwings', 0) * 5
            + item.get('hamburgers', 0) * 3
            + item.get('hotdogs', 0) * 2
        } for item in sorted(
            who_ate_what, key=lambda item: (
                -(item.get('chickenwings', 0) * 5
                + item.get('hamburgers', 0) * 3
                + item.get('hotdogs', 0) * 2),
                item['name']
            )
        )
    ]