"""Module of the perks factory"""

from business.perks.perk import Perk
from business.stats.stats import PlayerStats

class PerkFactory():
    """Represents the perks factory"""
    @staticmethod
    def create_perk(perk_name:str):
        """Adds a perk.
        
        Args:
            perk_name (str): The name of the perk.
        """
        if perk_name == "Speedy Boots":
            asset = "./assets/perks/Speedy Boots.png"
            max_level = 4
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Boosts your speed by 10%",
            "ATTRIBUTE": "movement_speed", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Boosts your speed by 15%",
            "ATTRIBUTE": "movement_speed",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.15
            },{"NAME":"Level 2",
            "DESCRIPTION": "Boosts your speed by 15%",
            "ATTRIBUTE": "movement_speed", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.15
            },{"NAME":"Level 3",
            "DESCRIPTION": "Boosts your speed by 20%",
            "ATTRIBUTE": "movement_speed", 
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)

        elif perk_name == "Sacred Heart":
            asset = "./assets/perks/Sacred Heart.png"
            max_level = 4
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Increases Regeneration rate in 10%",
            "ATTRIBUTE": "max_health", 
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

        elif perk_name == "Pizzano's Blessing":
            asset = "./assets/perks/Pizzano's Blessing.png"
            max_level = 3
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Increases Luck in 10%",
            "ATTRIBUTE": "luck", 
            "OPERATION":"SUM",
            "VALUE": 10
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Increases Luck in 25%",
            "ATTRIBUTE": "luck", 
            "OPERATION":"SUM",
            "VALUE": 25
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "Increases Luck in 25%",
            "ATTRIBUTE": "luck", 
            "OPERATION":"SUM",
            "VALUE": 25
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)

        elif perk_name == "Gym Power":
            asset = "./assets/perks/Gym Power.png"
            max_level = 5
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Increases damage in 10%",
            "ATTRIBUTE": "base_damage_multiplier", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Increases damage in 10%",
            "ATTRIBUTE": "base_damage_multiplier", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "Increases damage in 10%",
            "ATTRIBUTE": "base_damage_multiplier", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 3",
            "DESCRIPTION": "Increases damage in 10%",
            "ATTRIBUTE": "base_damage_multiplier", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 4",
            "DESCRIPTION": "Increases damage in 10%",
            "ATTRIBUTE": "base_damage_multiplier", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)

        elif perk_name == "Fast Hands":
            asset = "./assets/perks/Fast Hands.png"
            max_level = 5
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Increases attack speed in 10%",
            "ATTRIBUTE": "base_attack_speed", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Increases attack speed in 10%",
            "ATTRIBUTE": "base_attack_speed", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "Increases attack speed in 10%",
            "ATTRIBUTE": "base_attack_speed", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 3",
            "DESCRIPTION": "Increases attack speed in 10%",
            "ATTRIBUTE": "base_attack_speed", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            },
            {"NAME":"Level 4",
            "DESCRIPTION": "Increases attack speed in 10%",
            "ATTRIBUTE": "base_attack_speed", 
            "OPERATION":"SUM",
            "VALUE": 0.1
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)

        elif perk_name == "Heal Heal Frog's Booty":
            asset = "./assets/perks/Heal Heal Frog's Booty.png"
            max_level = 3
            perk_stats = PlayerStats()
            upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "Increases regeneration rate in 25%",
            "ATTRIBUTE": "regeneration_rate", 
            "OPERATION":"SUM",
            "VALUE": 2500
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "Increases regeneration rate in 25%",
            "ATTRIBUTE": "regeneration_rate", 
            "OPERATION":"SUM",
            "VALUE": 2500
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "Increases regeneration rate in 50%",
            "ATTRIBUTE": "regeneration_rate", 
            "OPERATION":"SUM",
            "VALUE": 5000
            }]
            return Perk(perk_name,max_level,upgrades,perk_stats,asset)
        else:
            raise ValueError
