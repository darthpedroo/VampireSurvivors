from business.entities.interfaces import IAttack


class Attack(IAttack):
    
    def is_attack_critical(self):
        return super().is_attack_critical()
    
    def is_cool_down_over(self):
        return super().is_cool_down_over()
    
    def perform_move(self, entity: "Entity"):
        return super().perform_move(entity)
    
    