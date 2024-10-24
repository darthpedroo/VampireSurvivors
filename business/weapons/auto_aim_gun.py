import math
from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld
from business.entities.item_factory import ProjectileFactory
from business.weapons.upgradable_weapon import UpgradableWeapon



class AutoAimGun(Weapon, UpgradableWeapon):
    def __init__(self, weapon_name:str, bullet_name: str, bullet_cooldown: int, bullet_speed: int):
        self.weapon_name = weapon_name
        self.__last_shot_time = 0
        self._base_shoot_cooldown = bullet_cooldown
        self.__bullet_name = bullet_name
        self.__speed = bullet_speed
        self._level = 2
        self._damage_multiplier = 1
        self._upgrades = [
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
            }]
        self.load_upgrades()
    
    def set_last_shot_time(self, new_time):
        self.__last_shot_time = new_time

    def is_cooldown_over(self, current_time):
        return current_time - self.__last_shot_time >= self._base_shoot_cooldown

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
        dir_x, dir_y = self.__calculate_direction(
            monster.pos_x-player_pos_x, monster.pos_y - player_pos_y)
        return dir_x, dir_y

    def __calculate_direction(self, dx, dy):
        distance = math.hypot(dx, dy)
        if distance != 0:
            return dx / distance, dy / distance
        return 0, 0

    def use(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time):
        projectile_factory = ProjectileFactory()
        try:
            bullet_direction_x, bullet_direction_y = self.aim(
                world, player_pos_x, player_pos_y)
            projectile = projectile_factory.create_item(
                self.__bullet_name, player_pos_x, player_pos_y, bullet_direction_x, bullet_direction_y, self.__speed, self._damage_multiplier, world)
            if self.is_cooldown_over(current_time):
                world.add_bullet(projectile)
                self.__last_shot_time = current_time
        except TypeError:
            print("There are no monsters yet...")

    @property
    def bullet_name(self):
        return self.__bullet_name

