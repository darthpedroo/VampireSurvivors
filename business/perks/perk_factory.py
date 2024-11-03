from business.perks.perk import Perk
from business.stats.stats import PlayerStats

class PerkFactory():
    @staticmethod
    def create_perk(perk_name:str):
        if perk_name == "Speedy Boots":
            asset = "./assets/perks/Speedy Boots.png"
            max_level = 2
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Boosts your speed by 10%",
            "ATTRIBUTE": "movement_speed", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Boosts your speed by 20%",
            "ATTRIBUTE": "movement_speed",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)
        else:
            raise ValueError

