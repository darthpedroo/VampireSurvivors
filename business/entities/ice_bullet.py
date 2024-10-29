"""Module for a bullet entity that moves towards a target direction."""

import math
import pygame

from business.entities.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite


class IceBullet(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, pos_x, pos_y, dir_x, dir_y, speed: int, health: int, damage_amount: int, asset: str, size):
        super().__init__(pos_x, pos_y, speed, BulletSprite(pos_x, pos_y, asset, size))
        self.__dir_x = dir_x
        self.__dir_y = dir_y
        self._logger.debug("Created %s", self)
        self._health = health
        self._damage_amount = damage_amount

    @property
    def health(self) -> int:  # Why does it have health ? :v
        return self._health

    def take_damage(self, amount):
        self._health -= amount

    def update(self, _: IGameWorld):
        self.move(self.__dir_x, self.__dir_y)

    @property
    def damage_amount(self):
        return self._damage_amount

    def __str__(self):
        return f"Bullet(pos=({self._pos_x, self._pos_y}), dir=({self.__dir_x, self.__dir_y}))"

    def apply_affect(self, other_entity: MovableEntity):
        ice_effect_duration = 100
        other_entity.apply_ice_effect(ice_effect_duration)