from app.models.riot import RiotId

def get_first_kills_all_time(riotId: RiotId, matches: list):
    fk = 0
    fb = 0

    for match in matches['data']:
        kills = match['kills']
        kills_by_round = {}
        for kill in kills:
            rnd = kill['round']
            if rnd not in kills_by_round:
                kills_by_round[rnd] = []
            kills_by_round[rnd].append(kill)
        
        for rnd_kills in kills_by_round.values():
            first_kill = rnd_kills[0]

            killer = first_kill['killer']
            victim = first_kill['victim']

            if killer['name'] == riotId['name'] and killer['tag'] == riotId['tag']:
                fk += 1
            elif victim['name'] == riotId['name'] and victim['tag'] == riotId['tag']:
                fb += 1
    return [fk, fb]