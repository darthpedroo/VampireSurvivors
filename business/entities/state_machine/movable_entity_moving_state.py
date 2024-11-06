"""Module that contains the MovableEntityMovingState class"""

from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState

class MovableEntityMovingState(MovableEntityBaseState):
    """Represents the moving state of a movable entity"""

    def update_state(self, movable_entity: "MovableEntity"):
        """Updates the position of the movable entity based on its direction and speed.

        Args:
            movable_entity (MovableEntity): The movable entity whose state is being updated.
        """
        if movable_entity._moving:
            movable_entity._pos_x += movable_entity.direction_x*movable_entity._stats.movement_speed
            movable_entity._pos_y += movable_entity.direction_y*movable_entity._stats.movement_speed

            movable_entity._sprite.update_pos(movable_entity._pos_x, movable_entity._pos_y)

            

    def enter_state(self, movable_entity: "MovableEntity"):
        """Enters the moving state for the given movable entity.

        Args:
            movable_entity (MovableEntity): The movable entity entering this state.
        """
        movable_entity.current_state = self
        movable_entity.set_moving(True)
        
