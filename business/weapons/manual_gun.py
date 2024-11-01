from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld


class ManualGun(Weapon):

    def __init__(self, weapon_name, bullet_name, bullet_cooldown, bullet_speed, max_level):
        super().__init__(weapon_name, bullet_name, bullet_cooldown, bullet_speed, max_level)
        self._upgrades = [{"NAME":"Level 0",
            "DESCRIPTION": "UNLOCKS THE WEAPON!",
            "ATTRIBUTE": "_level",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1  
            },{"NAME":"Level 1",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "_base_shoot_cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },
            {"NAME":"Level 2",
            "DESCRIPTION": "INCREASES 10% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "_damage_multiplier",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.1   
            },{"NAME":"Level 3",
            "DESCRIPTION": "REDUCES BULLET_COOLDOWN BY 10%",
            "ATTRIBUTE": "_base_shoot_cooldown",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 0.9  
            },{"NAME":"Level 4",
            "DESCRIPTION": "INCREASES 5% OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "_damage_multiplier",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.05   
            },{"NAME":"Level 5",
            "DESCRIPTION": "INCREASES 20 % OF GUN BASE_DAMAGE",
            "ATTRIBUTE": "_damage_multiplier",
            "OPERATION":"MULTIPLICATION",
            "VALUE": 1.2   
            }]
        
        self.load_upgrades()

    def aim(self, world: IGameWorld, player_pos_x: int, player_pos_y: int):
        mouse_pos_x, mouse_pos_y = world.get_mouse_position()
        camera_x = world.get_camera().camera_rect[0]
        camera_y = world.get_camera().camera_rect[1]
        dir_x, dir_y = self.calculate_direction(
            (mouse_pos_x + camera_x) - player_pos_x, (mouse_pos_y + camera_y) - player_pos_y)
        return dir_x, dir_y

