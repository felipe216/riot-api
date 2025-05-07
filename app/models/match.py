from dataclasses import dataclass

@dataclass
class Match:
    id: str
    rounds: list
    players: list
    map_name: str
    result: str