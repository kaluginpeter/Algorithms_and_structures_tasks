# You are the Dungeon Master for a public DnD game at your local comic shop and recently you've had some trouble keeping your players' info neat and organized so you've decided to write a bit of code to help keep them sorted!
#
# The goal of this code is to create an array of objects that stores a player's name and contact number from a given string.
#
# The method should return an empty array if the argument passed is an empty string or nil/None/null.
#
# Examples
# player_manager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{"player": "John Doe", "contact": 8167238327}, {"player": "Jane Doe", "contact": 8163723827}]
# player_manager(None) returns []
# player_manager("")   returns []
# playerManager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{player: "John Doe", contact: 8167238327}, {player: "Jane Doe", contact: 8163723827}]
# playerManager(null) returns []
# playerManager("")   returns []
# Have at thee!
#
# Arrays
# Solution
def player_manager(players):
    output: list[dict[str, str | int]] = []
    if not players: return output
    players = players.split(', ')
    for i in range(0, len(players), 2):
        output.append({"player": players[i], "contact": int(players[i + 1])})
    return output