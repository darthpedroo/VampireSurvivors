"""Module that contains the MovableEntityFrozenState class"""
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
from business.entities.state_machine.movable_entity_moving_state import MovableEntityMovingState
from business.handlers.cooldown_handler import CooldownHandler


class MovableEntityFrozenState(MovableEntityBaseState):
    """Represents the frozen state of a movable entity."""

    def update_state(self, movable_entity):
        """Update the state of the movable entity.

        Args:
            movable_entity: The movable entity to update.
        """
        if self.cooldown.is_action_ready():
            moving_state = MovableEntityMovingState()
            movable_entity.set_moving(True)
            moving_state.enter_state(movable_entity)
            movable_entity.sprite.restore_image()
        else:
            movable_entity.set_moving(False)
            movable_entity.sprite.freeze()

    def enter_state(self, movable_entity):
        """Enter the frozen state for the movable entity.

        Args:
            movable_entity: The movable entity entering the frozen state.
        """
        movable_entity.current_state = self
        self.cooldown = CooldownHandler(5000)
