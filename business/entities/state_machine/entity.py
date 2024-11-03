"""Contains the base classes for all entities in the game."""

import logging
from abc import abstractmethod

from business.entities.interfaces import ICanMove, IHasPosition, IHasSprite
from business.entities.state_machine.movable_entity_moving_state import MovableEntityMovingState
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
from business.entities.state_machine.movable_entity_frozen_state import MovableEntityFrozenState
from presentation.sprite import Sprite


class Entity(IHasPosition, IHasSprite):
    """Base class for all entities in the game."""

    def __init__(self, pos_x: float, pos_y: float, sprite: Sprite):
        """Initialize the entity with position and sprite.

        Args:
            pos_x (float): The position on the x axis of the entity.
            pos_y (float): The position on the y axis of the entity.
            sprite (Sprite): The sprite of the entity.
        """
        self._pos_x: float = pos_x
        self._pos_y: float = pos_y
        self._sprite: Sprite = sprite
        self._logger = logging.getLogger(self.__class__.__name__)

    def _get_distance_to(self, an_entity: IHasPosition) -> float:
        """Returns the distance to another entity.

        Args:
            an_entity (IHasPosition): The entity to calculate the distance to.

        Returns:
            float: The distance to the other entity.
        """
        return ((self.pos_x - an_entity.pos_x) ** 2 + (self.pos_y - an_entity.pos_y) ** 2) ** 0.5

    @property
    def pos_x(self) -> float:
        """Get the x axis of the entity."""
        return self._pos_x

    @property
    def pos_y(self) -> float:
        """Get the y axis of the entity."""
        return self._pos_y

    @property
    def sprite(self) -> Sprite:
        """Get the sprite of the entity."""
        return self._sprite

    @abstractmethod
    def __str__(self):
        """Returns a string representation of the entity."""

    def update(self):
        """Updates the entity."""
        self.sprite.update()


class MovableEntity(Entity, ICanMove):
    """Base class for all entities that can move."""

    def __init__(self, pos_x: float, pos_y: float, stats: float, sprite: Sprite, current_state = MovableEntityMovingState()): #pylint: disable=line-too-long
        """Initialize a movable entity with position, stats, and sprite.

        Args:
            pos_x (float): The x axis of the entity.
            pos_y (float): The y axis of the entity.
            stats (float): The stats of the entity.
            sprite (Sprite): The sprite if the entity.
            current_state (MovableEntityBaseState): The current state of the entity.
        """
        super().__init__(pos_x, pos_y, sprite)
        self._pos_x: float = pos_x
        self._pos_y: float = pos_y
        self._stats = stats
        self._sprite: Sprite = sprite
        self._moving = True
        self.current_state = current_state
        self.direction_x = 0.0
        self.direction_y = 0.0

    def set_moving(self, moving_state: bool):
        """Set the moving state of the entity.

        Args:
            moving_state (bool): The new moving state.
        """
        self._moving = moving_state

    def set_direction(self, direction_x: float, direction_y: float):
        """Set the direction that the entity is facing.

        Args:
            direction_x (float): The x-direction to face.
            direction_y (float): The y-direction to face.
        """
        self.direction_x = direction_x
        self.direction_y = direction_y

    def update(self):
        """Update the current state of the entity."""
        self.current_state.update_state(self)

    def switch_state(self, new_state: MovableEntityBaseState):
        """Switch to a new state.

        Args:
            new_state (MovableEntityBaseState): The new state to switch to.
        """
        new_state.enter_state(self)

    def apply_ice_effect(self, time):
        """Apply an ice effect to the entity, switching to frozen state.

        Args:
            time: The duration of the ice effect.
        """
        frozen_state = MovableEntityFrozenState()
        self.switch_state(frozen_state)

    @property
    def moving(self):
        """Get the moving state of the entity."""
        return self._moving
