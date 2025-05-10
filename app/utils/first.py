

def get_first_kills_all_time(puuid: str, data: dict):
    rounds = data['data']['rounds']

    if rounds:
        for round in rounds:
            if round['players']['all_players']:
                for player in round['players']['all_players']:
                    if player['puuid'] == puuid:
                        return player['first_kills']
    return None