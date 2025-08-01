# Get the list of integers for 'totalAuthored' and 'totalCompleted' of the nth ranker at Codewars Leaderboard.
#
# (1 <= n <= 500)
#
# See Example Test Cases for the expected data format.
#
# (Note 1 : Mind the title of this kata as well as https://dev.codewars.com/ )
#
# (Note 2 : It is recommended to finish Codewars Leaderboard before this kata. )
#
# Fundamentals
# Solution
from bs4 import BeautifulSoup
from requests import Response, get
def get_code_challenges(n: int) -> list[int]:
    response: Response = get('https://www.codewars.com/users/leaderboard')
    soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
    output: list[int] = []
    i: int = 0
    for user in soup.find('div', class_='leaderboard p-0').table:
        user_data: str = user.find('td', class_='is-big')
        if not user_data: continue
        print(user_data.a.text)
        i += 1
        if i != n: continue
        response_api: dict[str, int] = get(f'https://www.codewars.com/api/v1/users/{user_data.a.text}').json()['codeChallenges']
        return [response_api['totalAuthored'], response_api['totalCompleted']]