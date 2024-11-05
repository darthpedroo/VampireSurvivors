from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld
import time
import math
class NoAimGun(Weapon):
    def __init__(self, item_name, bullet_name, max_level, weapon_stats, level=1):
        super().__init__(item_name, bullet_name, max_level, weapon_stats, level)
        self.start_time = time.time()
        self.rotation_speed = 15
        self._level = level
        self._upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "UNLOCKS THE WEAPON!",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1
            },{"NAME":"Level 1",
            "DESCRIPTION": "INCREASES DAMAGE BY 10%",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "INCREASES DAMAGE BY 10%",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1
            },{"NAME":"Level 3",
            "DESCRIPTION": "INCREASES DAMAGE BY 10%",
            "ATTRIBUTE": "cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1  
            },{"NAME":"Level 4",
            "DESCRIPTION": "INCREASES DAMAGE BY 20%",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2
            }]
        self.load_upgrades(self._upgrades, self.level, self.item_stats)

    def aim (self, world: IGameWorld, player_pos_x: int, player_pos_y: int):
        # Calcular el tiempo transcurrido desde el inicio
        elapsed_time = time.time() - self.start_time
        # Calcular el ángulo actual basándonos en la velocidad de rotación y el tiempo
        angle = elapsed_time * self.rotation_speed

        radius = 90 #Harcoded Value: Fix Later

        dir_x = player_pos_x + radius * math.cos(angle)
        dir_y = player_pos_y + radius * math.sin(angle)

        return dir_x, dir_y