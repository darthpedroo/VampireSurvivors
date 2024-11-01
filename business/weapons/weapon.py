from abc import ABC, abstractmethod
from business.world.interfaces import IGameWorld
from business.entities.item_factory import ProjectileFactory
import math

class Weapon(ABC):
    def __init__(self, weapon_name:str, bullet_name: str, bullet_cooldown: int, bullet_speed: int, max_level:int):
        self.weapon_name = weapon_name
        self._last_shot_time = 0
        self._base_shoot_cooldown = bullet_cooldown
        self._bullet_name = bullet_name
        self._speed = bullet_speed
        self._level = 1
        self._max_level = max_level
        self._damage_multiplier = 1
        self._upgrades = []
        
    def is_cooldown_over(self, current_time):
        return current_time - self._last_shot_time >= self._base_shoot_cooldown
    
    def set_last_shot_time(self, new_time):
        self._last_shot_time = new_time
    
    def calculate_direction(self, dx, dy):
        distance = math.hypot(dx, dy)
        if distance != 0:
            return dx / distance, dy / distance
        return 0, 0
    
    def get_upgrade_info_by_level(self, level:int):
        
        try:
            level_info = self._upgrades[level]["DESCRIPTION"]
        except IndexError:
            print("ERROR CON EL INDEX!")
        
        return level_info
    
    def load_upgrades(self):
        for level in range(self._level):
            self.upgrade_level(level)
    
    def upgrade_level(self, level: int):
        
        current_upgrade = self._upgrades[level-1] #ojo
        attribute_to_modify = current_upgrade.get('ATTRIBUTE')
        new_value = current_upgrade.get('VALUE')
        if current_upgrade.get('OPERATION') == 'MULTIPLICATION':
            new_value = getattr(self, attribute_to_modify) * new_value
            setattr(self, attribute_to_modify, new_value)
    
    def upgrade_next_level(self):
        if self._level < self._max_level:
            self._level += 1
            self.upgrade_level(self._level)
        else:
            print("Max level acquired")
    
    def has_reached_max_level(self):
        return self._level == self._max_level


    def use(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time, player_damage_multiplier:int, player_attack_speed:int ):
        projectile_factory = ProjectileFactory()
        try:
            bullet_direction_x, bullet_direction_y = self.aim(world, player_pos_x, player_pos_y)
            projectile = projectile_factory.create_item(
                self._bullet_name, player_pos_x, player_pos_y, bullet_direction_x, bullet_direction_y, self._speed * player_attack_speed, self._damage_multiplier * player_damage_multiplier, world)
            if self.is_cooldown_over(current_time):
                world.add_bullet(projectile)
                self._last_shot_time = current_time
        except TypeError:
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
