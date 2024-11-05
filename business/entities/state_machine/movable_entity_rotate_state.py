import time
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState

class RotatingState(MovableEntityBaseState):
    def __init__(self, rotation_speed: float = 10):
        super().__init__()
        self.start_time = time.time()
        self.rotation_speed = rotation_speed


    def update_state(self, movable_entity: "MovableEntity"):
        movable_entity._pos_x = movable_entity.direction_x
        movable_entity._health -= 1 / movable_entity._health 
        movable_entity._pos_y = movable_entity.direction_y
        movable_entity._sprite.update_pos(movable_entity._pos_x, movable_entity._pos_y)
        

    def enter_state(self, movable_entity: "MovableEntity"):
        movable_entity.current_state = self
        movable_entity.set_moving(True)