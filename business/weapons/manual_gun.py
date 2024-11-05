"""Module of the Manual Gun weapon"""
from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld


class ManualGun(Weapon):
    """Represents the Manual Gun"""
    def __init__(self, item_name, bullet_name, max_level, weapon_stats, level=1):
        super().__init__(item_name, bullet_name, max_level, weapon_stats, level)
        self._level = level
        self._upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "UNLOCKS THE WEAPON!",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1  
            },{"NAME":"Level 1",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.01  
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "INCREASES 10% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1   
            },{"NAME":"Level 3",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 4",
            "DESCRIPTION": "INCREASES 5% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.05   
            },{"NAME":"Level 5",
            "DESCRIPTION": "INCREASES 20 % OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "damage",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2  
            }]
        
        self.load_upgrades(self._upgrades, self.level, self.item_stats)
        


    def aim(self, world: IGameWorld, pos_x: int, pos_y: int):
        mouse_pos_x, mouse_pos_y = world.get_mouse_position()
        camera_x = world.get_camera().camera_rect[0]
        camera_y = world.get_camera().camera_rect[1]
        dir_x, dir_y = self.calculate_direction(
            (mouse_pos_x + camera_x) - pos_x, (mouse_pos_y + camera_y) - pos_y)
        return dir_x, dir_y
