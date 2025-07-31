# Get the list of integers for Codewars Leaderboard score (aka Honor) in descending order
#
# Note:
# if it was the bad timing, the data could be updated during your test cases.
# Try several times if you had such experience.
# Fundamentals
# Solution
from bs4 import BeautifulSoup
from requests import Response, get
def get_leaderboard_honor() -> list[int]:
    response: Response = get('https://www.codewars.com/users/leaderboard')
    soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
    output: list[int] = []
    for user in soup.find('div', class_='leaderboard p-0').table:
        honor: str = user.find('td', class_='honor')
        if not honor: continue
        if not any(character.isdigit() for character in honor.text): continue
        output.append(int(honor.text.replace(',', '')))
    return output