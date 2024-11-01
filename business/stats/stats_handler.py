from abc import ABC

class BaseStats(ABC):
    """_summary_
    """
    def __init__(self, max_health: int, movement_speed:int, base_damage_multiplier: int, base_attack_speed:int):
        self.max_health = max_health
        self.movement_speed = movement_speed
        self.base_damage_multiplier = base_damage_multiplier
        self.base_attack_speed = base_attack_speed

class PlayerStats(BaseStats):
    """The Stats of a Player

    Args:
        BaseStats (_type_): _description_
    """
    def __init__(self, max_health, movement_speed, base_damage_multiplier, base_attack_speed, regeneration_rate: int, regeneration_percentage:int, xp_multiplier:int, luck:int):
        super().__init__(max_health, movement_speed, base_damage_multiplier, base_attack_speed)
        self.regeneration = regeneration_rate
        self.regeneration_percentage = regeneration_percentage
        self.xp_multiplier = xp_multiplier
        self.luck = luck


class MonsterStats(BaseStats):
    def __init__(self, max_health, movement_speed, base_damage_multiplier, base_attack_speed):
        super().__init__(max_health, movement_speed, base_damage_multiplier, base_attack_speed)




