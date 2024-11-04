"""Module of the Auto-Aim Gun"""
from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld

class AutoAimGun(Weapon):
    """Represents the Auto-Aim Gun"""
    def __init__(self, item_name, bullet_name, max_level, weapon_stats, level=1):
        super().__init__(item_name, bullet_name, max_level, weapon_stats, level)
        self._level = level
        self._upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "UNLOCKS THE WEAPON!",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1  
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "INCREASES 10% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1   
            },{"NAME":"Level 2",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 3",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 4",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 5",
            "DESCRIPTION": "INCREASES 20% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2   
            }]
        self.load_upgrades(self._upgrades, self.level, self.item_stats)

    def aim(self, world: IGameWorld, pos_x: int, pos_y: int):
        if not world.monsters:
            return
        monster = min(
            world.monsters,
            key=lambda monster: (
                (monster.pos_x - pos_x) ** 2 +
                (monster.pos_y - pos_y) ** 2
            ),
        )
        dir_x, dir_y = self.calculate_direction(
            monster.pos_x-pos_x, monster.pos_y - pos_y)
        return dir_x, dir_y
