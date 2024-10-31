"""Contains the base classes for all entities in the game."""

import logging
from abc import abstractmethod

from business.entities.interfaces import ICanMove, IDamageable, IHasPosition, IHasSprite
from business.world.interfaces import IGameWorld
from business.entities.state_machine.movable_entity_moving_state import MovableEntityMovingState
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
from business.entities.state_machine.movable_entity_frozen_state import MovableEntityFrozenState
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

    def update(self):
        """Updates the entity."""
        self.sprite.update()


class MovableEntity(Entity, ICanMove):
    """Base class for all entities that can move."""

    def __init__(self, pos_x: float, pos_y: float, speed: float, sprite: Sprite, current_state = MovableEntityMovingState()):
        super().__init__(pos_x, pos_y, sprite)
        self._pos_x: float = pos_x
        self._pos_y: float = pos_y
        self._speed: float = speed
        self._sprite: Sprite = sprite
        self._moving = True
        self.current_state = current_state
        self.direction_x = 0.0
        self.direction_y = 0.0
    
    def set_moving(self, moving_state: bool):
        self._moving = moving_state
    
    def set_direction(self, direction_x: float, direction_y: float):
        """Set the direction that the player is facing

        Args:
            direction_x (float):
            direction_y (float):
        """
        self.direction_x = direction_x
        self.direction_y = direction_y
    
    def update(self):
        self.current_state.update_state(self)
    
    def switch_state(self, new_state: MovableEntityBaseState):
        new_state.enter_state(self)
    
    def apply_ice_effect(self, time):
        frozen_state = MovableEntityFrozenState()
        self.switch_state(frozen_state)
        

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def moving(self):
        return self._moving