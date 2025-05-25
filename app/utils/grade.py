from app.models.riot import RiotId
from app.models.player import Player

from app.utils.first import get_first_kills_all_time

def calculate_grade(matches: list, riotId: RiotId):
    total_score = 0
    total_kills = 0
    total_deaths = 0
    total_assists = 0
    first_kills, first_deaths = get_first_kills_all_time(riotId, matches)
    for match in matches['data']:
        for player in match['players']:
            if player['tag'] == riotId['tag'] and player['name'] == riotId['name']:
                player['first_kills'] = first_kills
                player['first_deaths'] = first_deaths
                player = Player.from_dict(player)
                total_score += player.calculate_score()
                total_kills += player.kills
                total_deaths += player.deaths
                total_assists += player.assists
                break
    return {
        'total_score': (total_score*100).__round__(0),
        'total_kills': total_kills,
        'total_deaths': total_deaths,
        'total_assists': total_assists,
        'first_kills': first_kills,
        'first_deaths': first_deaths
    }