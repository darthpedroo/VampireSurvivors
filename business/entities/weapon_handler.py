import math
from abc import ABC, abstractmethod

from business.exceptions import ItemOverflow
from business.world.interfaces import IGameWorld
from business.weapons.weapon import Weapon
from business.entities.item_factory import ProjectileFactory
from business.weapons.weapon_factory import WeaponFactory
from business.entities.item_handler import ItemHandler


class WeaponHandler(ItemHandler):

    """Clase que permite manejar las distintas armas del jugador
    """

    def __init__(self, list_of_items =[] , max_items=5):
        super().__init__(list_of_items, max_items)

    def add_item(self, weapon_name: str):
        if len(self._list_of_items) <= self.max_items:
            weapon_factory = WeaponFactory()
            weapon = weapon_factory.create_weapon(weapon_name)
            self._list_of_items.append(weapon)
        else:
            raise ItemOverflow()

    def use_every_weapon(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time, player_base_damage_multiplier:int, player_base_attack_speed_multiplier:int):
        for weapon in self._list_of_items:
            weapon.use(player_pos_x, player_pos_y, world, current_time, player_base_damage_multiplier,player_base_attack_speed_multiplier)


