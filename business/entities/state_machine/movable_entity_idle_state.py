from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
class MovableEntityIdleState(MovableEntityBaseState):
    
    def update_state(self, movable_entity: "MovableEntity"):
        print("i am in the thick of it")
    
    def enter_state(self, movable_entity: "MovableEntity"):
        movable_entity.set_direction(0,0)
