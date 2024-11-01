import math
from abc import ABC, abstractmethod

from business.exceptions import WeaponOverflow
from business.world.interfaces import IGameWorld
from business.weapons.weapon import Weapon
from business.entities.item_factory import ProjectileFactory
from business.weapons.weapon_factory import WeaponFactory


class WeaponHandler():

    MAX_WEAPONS = 6
    """Clase que permite manejar las distintas armas del jugador
    """

    def __init__(self, list_of_weapons: list[Weapon] = []) -> None:
        self.__list_of_weapons = list_of_weapons

    def add_weapon(self, weapon_name: str):
        if len(self.__list_of_weapons) <= self.MAX_WEAPONS:
            weapon_factory = WeaponFactory()
            weapon = weapon_factory.create_weapon(weapon_name)
            self.__list_of_weapons.append(weapon)
        else:
            raise WeaponOverflow()

    def use_every_weapon(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time, player_base_damage_multiplier:int, player_base_attack_speed_multiplier:int):
        for weapon in self.__list_of_weapons:
            weapon.use(player_pos_x, player_pos_y, world, current_time, player_base_damage_multiplier,player_base_attack_speed_multiplier)

    def has_weapon(self, weapon_name:str):
        for weapon in self.__list_of_weapons:
            if weapon.weapon_name == weapon_name:
                return True
        return False
    
    def get_weapon_level(self, weapon_name:str):
        for weapon in self.__list_of_weapons:
            if weapon.weapon_name == weapon_name:
                return weapon.level
    
    def upgrade_weapon_next_level(self, weapon_name:str):
        for weapon in self.__list_of_weapons:
            if weapon.weapon_name == weapon_name:
                weapon.upgrade_next_level()
    
    def has_reached_max_level(self, weapon_name:str):
        for weapon in self.__list_of_weapons:
            if weapon.weapon_name == weapon_name:
                return weapon.has_reached_max_level()
