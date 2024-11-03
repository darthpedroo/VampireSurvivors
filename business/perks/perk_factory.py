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
        
        elif perk_name == "Sacred Heart":    
            asset = "./assets/perks/Sacred Heart.png"
            max_level = 3
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Increases Regeneration rate in 10%",
            "ATTRIBUTE": "regeneration_rate", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Increases 20% of Max Health",
            "ATTRIBUTE": "regeneration_rate", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "Increases 20% of Max Health",
            "ATTRIBUTE": "max_health", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2
            },
            {"NAME":"Level 3",
            "DESCRIPTION": "Doubles your max Health",
            "ATTRIBUTE": "max_health", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 2
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)
        else:
            raise ValueError

