"""Module that contains the MovableEntityIdleState class."""

from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState

class MovableEntityIdleState(MovableEntityBaseState):
    """Represents the idle state of a movable entity."""

    def update_state(self, movable_entity: "MovableEntity"):
        """Updates the state of the movable entity while it is idle.

        Args:
            movable_entity (MovableEntity): The movable entity in the idle state.
        """
        print("I am in the thick of it, everybody knows")

    def enter_state(self, movable_entity: "MovableEntity"):
        """Enters the idle state for the given movable entity.

        Args:
            movable_entity (MovableEntity): The movable entity entering this state.
        """
        movable_entity.set_direction(0, 0)
