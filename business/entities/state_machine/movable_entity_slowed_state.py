"""Module that contains the MovableEntityFrozenState class"""
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
from business.entities.state_machine.movable_entity_moving_state import MovableEntityMovingState
from business.handlers.cooldown_handler import CooldownHandler


class MovableEntitySlowedState(MovableEntityBaseState):
    """Represents the frozen state of a movable entity."""

    def update_state(self, movable_entity):
        if self.cooldown.is_action_ready():
            moving_state = MovableEntityMovingState()
            movable_entity._stats.movement_speed = self.old_stats
            movable_entity.switch_state(moving_state)
            movable_entity.sprite.restore_image()
            movable_entity.set_direction(10,10)
        else:
            movable_entity.sprite.freeze()
            if movable_entity._moving:
                movable_entity._pos_x += movable_entity.direction_x*movable_entity._stats.movement_speed
                movable_entity._pos_y += movable_entity.direction_y*movable_entity._stats.movement_speed
                movable_entity._sprite.update_pos(movable_entity._pos_x, movable_entity._pos_y)

    def enter_state(self, movable_entity):
        self.old_stats = movable_entity._stats.movement_speed
      
        movable_entity._stats.movement_speed = movable_entity._stats.movement_speed /2 
        """Enter the frozen state for the movable entity.

        Args:
            movable_entity: The movable entity entering the frozen state.
        """
        movable_entity.current_state = self
        self.cooldown = CooldownHandler(2000)
