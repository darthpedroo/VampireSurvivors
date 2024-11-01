from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
# from business.entities.state_machine.entity import MovableEntity


class MovableEntityMovingState(MovableEntityBaseState):

    def update_state(self, movable_entity: "MovableEntity"):
        if movable_entity._moving:

            movable_entity._pos_x += movable_entity.direction_x * movable_entity._speed
            movable_entity._pos_y += movable_entity.direction_y * movable_entity._speed

            movable_entity._sprite.update_pos(
                movable_entity._pos_x, movable_entity._pos_y)

    def enter_state(self, movable_entity: "MovableEntity"):
        movable_entity.current_state = self
        movable_entity.set_moving(True)
