import requests
from bs4 import BeautifulSoup

from config import SCRAPING_URL, MESSAGES, TEAM

# Functions
def run():
    soup = get_page()
    if(soup == None):
        return MESSAGES["error-scrapping"]

    teams = get_teams(soup)
    message = team_plays(teams)
    return message


def get_page():
    if(SCRAPING_URL == None):
        return None
    
    page = requests.get(SCRAPING_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    return soup


def get_teams(soup):
    teams = soup.find_all("span", { "class": "datoequipo" })
    teamNames = set()

    for team in teams:
        teamNames.add(team.text.upper())

    return list(teamNames)


def team_plays(teams):
    filterTeam = filter(lambda team: team == TEAM, teams)

    if(filterTeam):
        return MESSAGES["plays"]
    else:
        return MESSAGES["doesnt-play"]


if __name__ == '__main__':
    run()
