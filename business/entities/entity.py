"""Contains the base classes for all entities in the game."""

import logging
from abc import abstractmethod

from business.entities.interfaces import ICanMove, IDamageable, IHasPosition, IHasSprite
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite


class Entity(IHasPosition, IHasSprite):
    """Base class for all entities in the game."""

    def __init__(self, pos_x: float, pos_y: float, sprite: Sprite):
        self._pos_x: float = pos_x
        self._pos_y: float = pos_y
        self._sprite: Sprite = sprite
        self._logger = logging.getLogger(self.__class__.__name__)

    def _get_distance_to(self, an_entity: IHasPosition) -> float:
        """Returns the distance to another entity using the Euclidean distance formula.

        Args:
            an_entity (IHasPosition): The entity to calculate the distance to.
        """
        return ((self.pos_x - an_entity.pos_x) ** 2 + (self.pos_y - an_entity.pos_y) ** 2) ** 0.5

    @property
    def pos_x(self) -> float:
        return self._pos_x

    @property
    def pos_y(self) -> float:
        return self._pos_y

    @property
    def sprite(self) -> Sprite:
        return self._sprite

    @abstractmethod
    def __str__(self):
        """Returns a string representation of the entity."""

    def update(self, world: IGameWorld):
        """Updates the entity."""
        self.sprite.update()


class MovableEntity(Entity, ICanMove):
    """Base class for all entities that can move."""

    def __init__(self, pos_x: float, pos_y: float, speed: float, sprite: Sprite):
        super().__init__(pos_x, pos_y, sprite)
        self._pos_x: float = pos_x
        self._pos_y: float = pos_y
        self._speed: float = speed
        self._sprite: Sprite = sprite

    def move(self, direction_x: float, direction_y: float):
        self._pos_x += direction_x * self._speed
        self._pos_y += direction_y * self._speed
        
        self._logger.debug(
            "Moving in direction (%.2f, %.2f) with speed %.2f",
            direction_x,
            direction_y,
            self._speed,
        )
        
        self.sprite.update_pos(self._pos_x, self._pos_y)

    @property
    def speed(self) -> float:
        return self._speed