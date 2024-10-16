"""Module for a bullet entity that moves towards a target direction."""

import math

from business.entities.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletGuidedSprite
from presentation.display import Display


class BulletGuided(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, src_x, src_y, speed, world):            
        super().__init__(src_x, src_y, speed, BulletGuidedSprite(src_x, src_y))
        self._player_pos = (src_x, src_y)
        self.__mouse_pos = self.__get_mouse_position(world)
        self.__dir_x, self.__dir_y = self.__calculate_direction((self.__mouse_pos[0] + world.get_camera().camera_rect[0]) - src_x, (self.__mouse_pos[1] + world.get_camera().camera_rect[1]) - src_y)
        self._logger.debug("Created %s", self)
        self._health = 500
        print("self._camera.camera_rect[0]", world.get_camera().camera_rect[0])
        
    def __get_mouse_position(self, world: IGameWorld) -> tuple[int,int] :
        return world.get_mouse_position()

    def __calculate_direction(self, dx, dy):
        distance = math.hypot(dx, dy)
        if distance == 0:
            return 0, 0  # Prevents division by zero
        return dx / distance, dy / distance  # Normalized vector


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
