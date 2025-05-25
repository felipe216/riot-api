from app.models.riot import RiotId
from app.models.player import Player


def calculate_grade(matches: list, riotId: RiotId):
    total_score = 0
    total_kills = 0
    total_deaths = 0
    total_assists = 0
    for match in matches['data']:
        for player in match['players']:
            if player['tag'] == riotId['tag'] and player['name'] == riotId['name']:
                player['first_kills'] = 1
                player['first_deaths'] = 0
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
        'total_assists': total_assists
    }