from dataclasses import dataclass

@dataclass
class Player:
    def __init__(self, name, tag, team, character, tier, stats, ability_casts, damage_made, damage_received, behaviour, first_kills, first_deaths):
        self.name = name
        self.tag = tag
        self.team = team
        self.character = character
        self.tier = tier
        self.kills = stats["kills"]
        self.deaths = stats["deaths"]
        self.assists = stats["assists"]
        self.score = stats["score"]
        self.bodyshots = stats["bodyshots"]
        self.headshots = stats["headshots"]
        self.legshots = stats["legshots"]
        self.c_cast = ability_casts["c_cast"]
        self.q_cast = ability_casts["q_cast"]
        self.e_cast = ability_casts["e_cast"]
        self.x_cast = ability_casts["x_cast"]
        self.damage_made = damage_made
        self.damage_received = damage_received
        self.afk_rounds = behaviour["afk_rounds"]
        self.friendly_fire_in = behaviour["friendly_fire"]["incoming"]
        self.friendly_fire_out = behaviour["friendly_fire"]["outgoing"]
        self.first_kills = first_kills
        self.first_deaths = first_deaths
        
        # Métricas calculadas
        self.kda_score = self.calculate_kda_score()
        self.accuracy_score = self.calculate_accuracy_score()
        self.damage_score = self.damage_made - self.damage_received
        self.utility_score = self.c_cast + self.q_cast + self.e_cast + self.x_cast
        self.behaviour_score = self.afk_rounds + self.friendly_fire_in + self.friendly_fire_out
        self.fb_fd_score = self.first_kills - self.first_deaths
        self.score = self.calculate_score()
    
    def calculate_kda_score(self):
        return (self.kills + 0.5 * self.assists) / (self.deaths if self.deaths != 0 else 1)
    
    def calculate_accuracy_score(self):
        total_shots = self.headshots + self.bodyshots + self.legshots
        return self.bodyshots / total_shots if total_shots > 0 else 1

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        return cls(
            name=data["name"],
            tag=data["tag"],
            team=data["team"],
            character=data["character"],
            tier=data["currenttier_patched"],
            stats=data["stats"],
            ability_casts=data["ability_casts"],
            damage_made=data["damage_made"],
            damage_received=data["damage_received"],
            behaviour=data["behaviour"],
            first_kills=data["first_kills"],
            first_deaths=data["first_deaths"]
        )
    
    def calculate_score(self):
        return (
            2 * self.kda_score +
            1 * (1 - self.accuracy_score) +
            0.01 * self.damage_score +
            0.05 * self.utility_score -
            1.0 * self.behaviour_score +
            1.5 * self.fb_fd_score
        )