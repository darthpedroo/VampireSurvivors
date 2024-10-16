"""Module for a bullet entity that moves towards a target direction."""

import math

from business.entities.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite


class Bullet(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, src_x, src_y, speed, world):
        super().__init__(src_x, src_y, speed, BulletSprite(src_x, src_y))
        self.__nearest_enemy = self.__get_nearest_enemy(world)
        self.__dir_x, self.__dir_y = self.__calculate_direction(self.__nearest_enemy.pos_x - src_x, self.__nearest_enemy.pos_y - src_y)
        self._logger.debug("Created %s", self)
        self._health = 500
        
    def __get_nearest_enemy(self, world: IGameWorld):
        if not world.monsters:
            return
        
        monster = min(
            world.monsters,
            key=lambda monster: (
                (monster.pos_x - self.pos_x) ** 2 + (monster.pos_y - self.pos_y) ** 2
            ),
        )
        
        return monster

    def __calculate_direction(self, dx, dy):
        distance = math.hypot(dx, dy)
        if distance != 0:
            return dx / distance, dy / distance
        return 0, 0

    @property
    def health(self) -> int: #Why does it have health ? :v
        return self._health

    def take_damage(self, amount):
        self._health -= amount

    def update(self, _: IGameWorld):
        # Move bullet towards the target direction
        self.move(self.__dir_x, self.__dir_y)

    @property
    def damage_amount(self):
        return 0.10

    def __str__(self):
        return f"Bullet(pos=({self._pos_x, self._pos_y}), dir=({self.__dir_x, self.__dir_y}))"
