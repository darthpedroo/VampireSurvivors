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

    def use_every_weapon(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time):
        for weapon in self.__list_of_weapons:
            weapon.use(player_pos_x, player_pos_y, world, current_time)
