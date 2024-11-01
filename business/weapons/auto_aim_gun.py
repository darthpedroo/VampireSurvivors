
from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld



class AutoAimGun(Weapon):
    def __init__(self, weapon_name, bullet_name, bullet_cooldown, bullet_speed, max_level):
        super().__init__(weapon_name, bullet_name, bullet_cooldown, bullet_speed, max_level)
        self._upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "UNLOCKS THE WEAPON!",
            "ATTRIBUTE": "_level",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1  
            },
            {"NAME":"Level 1",
            "DESCRIPTION": "INCREASES 10% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "_damage_multiplier",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1   
            },{"NAME":"Level 2",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "_base_shoot_cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 3",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "_base_shoot_cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 4",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "_base_shoot_cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 5",
            "DESCRIPTION": "INCREASES 20% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "_damage_multiplier",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2   
            }]
        self.load_upgrades()
    
    def aim(self, world: IGameWorld, player_pos_x: int, player_pos_y: int):
        if not world.monsters:
            return
        monster = min(
            world.monsters,
            key=lambda monster: (
                (monster.pos_x - player_pos_x) ** 2 +
                (monster.pos_y - player_pos_y) ** 2
            ),
        )
        dir_x, dir_y = self.calculate_direction(
            monster.pos_x-player_pos_x, monster.pos_y - player_pos_y)
        return dir_x, dir_y

