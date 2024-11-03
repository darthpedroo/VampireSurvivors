"""Module that contains the MovableEntityBaseState"""

from abc import ABC, abstractmethod
class MovableEntityBaseState(ABC):
    """Represents the base state of a movable entity"""
    @abstractmethod
    def enter_state(self, movable_entity: "MovableEntity"):
        """Makes a movable entity enter a specific state

        Args:
            movable_entity (MovableEntity)
        """

    @abstractmethod
    def update_state(self, movable_entity: "MovableEntity"):
        """Updates the current state of the entity

        Args:
            movable_entity (MovableEntity):
        """
    