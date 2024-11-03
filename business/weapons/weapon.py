"""Module of the weapons"""

import math
from abc import abstractmethod
from business.entities.interfaces import UpgradableItem
from business.world.interfaces import IGameWorld
from business.entities.item_factory import ProjectileFactory
from business.stats.stats import WeaponStats

class Weapon(UpgradableItem):
    """Represents the weapons"""
    def __init__(self, item_name, bullet_name:str, max_level, weapon_stats:WeaponStats):
        super().__init__(item_name, max_level)
        self._bullet_name = bullet_name
        self.item_stats = weapon_stats
        self._last_shot_time = 0

    def is_cooldown_over(self, current_time):
        """Checks if the cooldown of the weapon is over.
        
        Args:
            current_time: The current time.
        """
        return current_time - self._last_shot_time >= self.item_stats.cooldown

    def set_last_shot_time(self, new_time):
        """Sets the last time the weapon is shot.
        
        Args:
            new_time: The new time that will be set as the last time the weapon was shot.
        """
        self._last_shot_time = new_time

    def calculate_direction(self, dx, dy):
        """Calculates the direction where the weapon should be shot.
        
        Args:
            dx: The direction on the x axis.
            dy: The direction on the y axis.
        """
        distance = math.hypot(dx, dy)
        if distance != 0:
            return dx / distance, dy / distance
        return 0, 0

    def use(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time, player_damage_multiplier: int, player_attack_speed:int): #pylint: disable=line-too-long, too-many-arguments
        """Uses the weapon.
        
        Args:
            player_pos_x (int): The player position on the x axis.
            player_pos_y (int): The player position on the y axis.
            world (IGameWorld): The game world.
            current_time: The current time.
            player_damage_multiplier (int): The player damage multiplier.
            player_attack_speed (int): The player attack speed.
        """
        #ISSUE! PASAR TODAS LAS ESTADISTICAS
        projectile_factory = ProjectileFactory()
        try:
            bullet_direction_x, bullet_direction_y = self.aim(world, player_pos_x, player_pos_y)

            movement_speed = self.item_stats.movement_speed
            damage = self.item_stats.damage * player_damage_multiplier
            cooldown = self.item_stats.cooldown * player_attack_speed

            projectile = projectile_factory.create_item(self._bullet_name,
                                                        player_pos_x,
                                                        player_pos_y,
                                                        bullet_direction_x,
                                                        bullet_direction_y,
                                                        movement_speed,
                                                        damage,cooldown)

            if self.is_cooldown_over(current_time):
                world.add_bullet(projectile)
                self._last_shot_time = current_time
        except TypeError:
            print("There are no monsters yet...")

    @property
    def bullet_name(self):
        """Returns the level bullet name of the weapon"""
        return self._bullet_name

    @property
    def level(self):
        """Returns the level of the weapon"""
        return self._level

    @abstractmethod
    def aim(self, world, pos_x, pos_y):
        """Gets the direction where the weapon should aim.
        
        Args:
            world: The game world.
            pos_x: The position on the x axis where the weapon should be aimed.
            pos_y: The position on the y axis where the weapon should be aimed.
        """

    def load_weapon_data(self, weapon_dao):
        """Loads the data of the weapon.

        Args:
            weapon_dao (_type_): _description_
        """
