"""Module of the weapons"""

import math
from abc import abstractmethod
from business.entities.interfaces import UpgradableItem
from business.world.interfaces import IGameWorld
from business.entities.item_factory import ProjectileFactory
from business.stats.stats import WeaponStats
from business.handlers.cooldown_handler import CooldownHandler

class Weapon(UpgradableItem):
    """Represents the weapons"""
    def __init__(self, item_name, bullet_name, max_level,weapon_stats: WeaponStats, level = 1):
        super().__init__(item_name, max_level, level)
        super().__init__(item_name, max_level)
        self._bullet_name = bullet_name
        self.item_stats = weapon_stats
        self._cooldown_handler = CooldownHandler(self.item_stats.cooldown)

    
    def create_weapon_json_data(self):
        weapon_data = {"item_name": self.item_name, "bullet_name": self.bullet_name, "level": self._level, "max_level": self._max_level, "item_stats": self.item_stats.create_weapon_stats_json_data()}
        return weapon_data

    def get_sprite(self):
        current_bullet = ProjectileFactory().create_item(self._bullet_name)
        return current_bullet.sprite.asset

    def is_cooldown_over(self):
        """Checks if the cooldown of the weapon is over.
        
        Args:
            current_time: The current time.
        """
        return self._cooldown_handler.is_action_ready()



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

            if self.is_cooldown_over():
                world.add_bullet(projectile)
                self._cooldown_handler.put_on_cooldown()

        except TypeError as err:
            print(err)

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
