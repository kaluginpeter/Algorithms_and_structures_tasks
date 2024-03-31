open_matches_by_player: dict = dict()
count_matches: dict = dict()
teams: list = list()
players_in_team: dict = dict()
goals_by_player: dict = dict()


def total_goals_of_team(team_name: str) -> int:
    count: int = 0
    for player_name in players_in_team.get(team_name, []):
        count += len(goals_by_player.get(player_name, []))
    return count


def mean_goals_per_game_by_team(team_name: str) -> float:
    """"Guaranteed that team have at least one played game"""
    return total_goals_of_team(team_name) / count_matches.get(team_name)


def total_goals_by_player(player_name: str) -> int:
    return len(goals_by_player.get(player_name, []))


def mean_goals_per_game_by_player(player_name: str) -> float:
    """Guaranteed that player have at least one goal"""
    for team_name in teams:
        if player_name in players_in_team.get(team_name, []):
            return total_goals_by_player(player_name) / count_matches.get(team_name)


def goals_on_minute_by_player(player_name: str, minute: int) -> int:
    count: int = 0
    for goal_minute in goals_by_player.get(player_name, []):
        if goal_minute == minute:
            count += 1
    return count


def goals_on_first_minutes_by_player(player_name: str, minute: int) -> int:
    count: int = 0
    for goal_minute in goals_by_player.get(player_name, []):
        if goal_minute <= minute:
            count += 1
    return count


def goals_on_last_minutes_by_player(player_name: str, minute: int) -> int:
    count: int = 0
    lower_boundary: int = 91 - minute
    for goal_time in goals_by_player.get(player_name, []):
        if lower_boundary <= goal_time <= 90:
            count += 1
    return count


def score_opens_by_team(team_name: str) -> int:
    count: int = 0
    for player_name in players_in_team.get(team_name, []):
        count += open_matches_by_player.get(player_name, 0)
    return count


def score_opens_by_player(player_name: str) -> int:
    return open_matches_by_player.get(player_name, 0)


answers: list = list()
reader = open('input.txt', 'r')
query: list = [i[:-1] for i in reader.readlines() if i.endswith('\n')]
reader.close()
for single_string in query:
    if single_string.startswith('"'):
        first_team: str = single_string[
                          single_string.index('"') + 1:single_string.index('"', single_string.index('"') + 1)]
        single_string = single_string[single_string.index('"', 2) + 1:]
        second_team: str = single_string[
                           single_string.index('"') + 1:single_string.index('"', single_string.index('"') + 1)]
        if first_team not in teams:
            teams.append(first_team)
            players_in_team[first_team] = []
        if second_team not in teams:
            teams.append(second_team)
            players_in_team[second_team] = []
        count_matches[first_team] = count_matches.get(first_team, 0) + 1
        count_matches[second_team] = count_matches.get(second_team, 0) + 1
        initially_goals_first_team, initially_goals_second_team = map(int, single_string.split()[-1].split(':'))
        goals_first_team, goals_second_team = initially_goals_first_team, initially_goals_second_team
    elif single_string.endswith("'"):
        if initially_goals_first_team == goals_first_team and initially_goals_second_team == goals_second_team:
            open_goal_time, open_goal_name = float('inf'), ''
        player_name: str = ' '.join(single_string.split()[:-1])
        goal_minute: int = int(single_string.split()[-1][:-1])
        goals_by_player[player_name] = goals_by_player.get(player_name, []) + [goal_minute]
        if goals_first_team > 0:
            if goals_first_team == initially_goals_first_team:
                if goal_minute < open_goal_time:
                    open_goal_time, open_goal_name = goal_minute, player_name
            if player_name not in players_in_team[first_team]:
                players_in_team[first_team] = players_in_team.get(first_team, []) + [player_name]
            goals_first_team -= 1
        else:
            if goals_second_team == initially_goals_second_team:
                if goal_minute < open_goal_time:
                    open_goal_time, open_goal_name = goal_minute, player_name
            if player_name not in players_in_team[second_team]:
                players_in_team[second_team] = players_in_team.get(second_team, []) + [player_name]
            goals_second_team -= 1
        if goals_first_team == 0 and goals_second_team == 0:
            open_matches_by_player[open_goal_name] = open_matches_by_player.get(open_goal_name, 0) + 1
    elif single_string.startswith('Total goals for'):
        answers.append(total_goals_of_team(
            single_string[single_string.index('"') + 1:single_string.index('"', single_string.index('"') + 1)]))
    elif single_string.startswith('Mean goals per game for'):

        answers.append(round(mean_goals_per_game_by_team(
            single_string[single_string.index('"') + 1:single_string.index('"', single_string.index('"') + 1)]), 3))
    elif single_string.startswith('Total goals by'):
        answers.append(total_goals_by_player(single_string.split(' by ')[-1]))
    elif single_string.startswith('Mean goals per game by'):
        answers.append(round(mean_goals_per_game_by_player(player_name=single_string.split(' by ')[-1]), 3))
    elif single_string.startswith('Goals on minute'):
        sliced_string: list = single_string.split('Goals on minute ')[1].split(' by ')
        answers.append(round(goals_on_minute_by_player(player_name=sliced_string[-1], minute=int(sliced_string[0])), 3))
    elif single_string.startswith('Goals on first'):
        sliced_string: list = single_string.split('Goals on first ')[1].split(' by ')
        answers.append(goals_on_first_minutes_by_player(player_name=sliced_string[-1],
                                                        minute=int(sliced_string[0].split(' minutes')[0])))
    elif single_string.startswith('Goals on last'):
        sliced_string: list = single_string.split('Goals on last ')[1].split(' by ')
        answers.append(goals_on_last_minutes_by_player(player_name=sliced_string[-1],
                                                       minute=int(sliced_string[0].split(' minutes')[0])))
    elif single_string.startswith('Score opens by "'):
        team_name: str = single_string[
                         single_string.index('"') + 1:single_string.index('"', single_string.index('"') + 1)]
        answers.append(score_opens_by_team(team_name=team_name))
    elif single_string.startswith('Score opens by '):
        answers.append(score_opens_by_player(player_name=single_string.split('Score opens by ')[1]))
print('\n'.join(str(i) for i in answers))