from abc import ABC, abstractmethod
from business.entities.interfaces import UpgradableItem
from business.world.interfaces import IGameWorld
from business.entities.item_factory import ProjectileFactory
from business.stats.stats import BulletStats, WeaponStats
import math

class Weapon(UpgradableItem):

    def __init__(self, item_name, bullet_name:str, max_level, weapon_stats:WeaponStats):
        super().__init__(item_name, max_level)
        self._bullet_name = bullet_name
        self.item_stats = weapon_stats
        self._last_shot_time = 0

    def is_cooldown_over(self, current_time):
        return current_time - self._last_shot_time >= self.item_stats.cooldown
    
    def set_last_shot_time(self, new_time):
        self._last_shot_time = new_time
    
    def calculate_direction(self, dx, dy):
        distance = math.hypot(dx, dy)
        if distance != 0:
            return dx / distance, dy / distance
        return 0, 0

    def use(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time, player_damage_multiplier:int, player_attack_speed:int): #ISSUE! PASAR TODAS LAS ESTADISTICAS 
        projectile_factory = ProjectileFactory()
        try:
            bullet_direction_x, bullet_direction_y = self.aim(world, player_pos_x, player_pos_y)
            
        #  projectile = projectile_factory.create_item(
          #      self._bullet_name, player_pos_x, player_pos_y, bullet_direction_x, bullet_direction_y, self.item_stats * player_attack_speed, self.item_stats * player_damage_multiplier, world)
            
            movement_speed = self.item_stats.movement_speed
            damage = self.item_stats.damage * player_damage_multiplier
            cooldown = self.item_stats.cooldown * player_attack_speed
            
            
            
            projectile = projectile_factory.create_item(
                self._bullet_name, player_pos_x, player_pos_y, bullet_direction_x, bullet_direction_y, movement_speed, damage,cooldown)
            
            if self.is_cooldown_over(current_time):
                world.add_bullet(projectile)
                self._last_shot_time = current_time
        except ZeroDivisionError:
            print("There are no monsters yet...")

    @property
    def bullet_name(self):
        return self._bullet_name
    
    @property
    def level(self):
        return self._level

    @abstractmethod
    def aim(self, world, pos_x, pos_y):
        """Gets the direction where the weapon should aim
        """
        pass

    def load_weapon_data(self, weapon_dao):
        """Loads the data of the weapon

        Args:
            weapon_dao (_type_): _description_
        """
        pass
